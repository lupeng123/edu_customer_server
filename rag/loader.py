from langchain_community.document_loaders import PyPDFLoader, TextLoader, CSVLoader
from langchain_core.documents import Document
from pathlib import Path

def load_file(file_path: str) -> list[Document]:
    p = Path(file_path)
    suffix = p.suffix.lower()
    if suffix == ".pdf":
        loader = PyPDFLoader(file_path)
    elif suffix == ".csv":
        loader = CSVLoader(file_path)
    elif suffix == ".txt":
        loader = TextLoader(file_path, encoding="utf-8")
    else:
        raise ValueError("不支持该文件类型，仅支持 pdf / csv / txt")
    docs = loader.load()
    # 增加元数据，记录来源文件名，RAG溯源
    for doc in docs:
        doc.metadata["source"] = p.name
    return docs
