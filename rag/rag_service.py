from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from model.model_factory import chat_model,chat_flash_model
from rag.vector_store import retriever
from utils.prompt_handler import load_rag_prompt,load_rag_extract_prompt


def print_prompt(prompt: str):
    # print("=" * 20)
    # print(prompt)
    # print("=" * 20)
    return prompt

class RagService(object):
    def __init__(self):
        self.prompt_template = PromptTemplate.from_template(load_rag_prompt())
        self.prompt_extract = PromptTemplate.from_template(load_rag_extract_prompt())
        self.retriever = retriever
        self.model = chat_model
        self.model_flash = chat_flash_model
        self.chain = self.get_chain()
        self.chain_extract = self.get_chain_extract()



    def get_chain(self):
        return self.prompt_template | print_prompt | self.model | StrOutputParser()

    def get_chain_extract(self):
        return self.prompt_extract | print_prompt | self.model_flash | StrOutputParser()


    def rag_summarize(self,query:str) -> str:
        res_doc = self.retriever.invoke(query)

        context = ""
        count = 0
        for doc in res_doc:
            count += 1
            context += f"【参考资料{count}】：参考资料：{doc.page_content} | 参考元数据：{doc.metadata}\n"

        # 拿父文档重新交给llm来提取有用信息
        res_extract = self.chain_extract.invoke(
            {
                "input": query,
                "context": context,
            }
        )

        return self.chain.invoke(
            {
                "input": query,
                "context": res_extract,
            }
        )

if __name__ == '__main__':
    rag = RagService()
    res = rag.rag_summarize("语文 A 班上课时间？")
    print(f"res:   {res}")