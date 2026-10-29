import asyncio
from langchain.agents import create_agent
from langchain_core.messages import AIMessage
from langgraph.checkpoint.memory import InMemorySaver
from model.model_factory import chat_model
from utils.prompt_handler import load_system_prompt
from agent.tools.agent_tool import tools
from agent.tools.middleware import middlewares


checkpointer = InMemorySaver()

class ReactAgent(object):

    def __init__(self):
        self.agent = create_agent(
            model=chat_model,
            system_prompt=load_system_prompt(),
            tools=tools,
            middleware=middlewares,
            checkpointer=checkpointer
        )

    async def ainvoke_message(self,query: str, session_id: str = None):
        input_data = {
            "messages": [
                {"role": "user", "content": query}
            ]
        }
        config = {}
        if session_id:
            config["configurable"] = {"thread_id": session_id}

        res_state = await self.agent.ainvoke(input_data,config=config)
        print(res_state)
        messages = res_state["messages"]
        last_msg = messages[-1]
        return last_msg.content

    async def astream_message(self, query: str, session_id: str = None):
        input_data = {
            "messages": [
                {"role": "user", "content": query}
            ]
        }
        config = {}
        if session_id:
            config["configurable"] = {"thread_id": session_id}

        async for msg_chunk in self.agent.astream(
                input_data,
                config=config,
                stream_mode="messages"
        ):
            msj = msg_chunk[0]
            if isinstance(msj, AIMessage) and msj.content.strip():
                yield msj.content



if __name__ == '__main__':
    agent = ReactAgent()

    res = asyncio.run(agent.ainvoke_message("春季语文培优班一共多少次课?"))
    print(res)