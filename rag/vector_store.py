import json
from fastapi import UploadFile
import tempfile
import os
from pathlib import Path
from rag.loader import load_file
from langchain_community.vectorstores import Chroma
from langchain_classic.retrievers import ParentDocumentRetriever
from langchain_classic.storage import InMemoryStore, EncoderBackedStore
from langchain_community.storage import RedisStore
from rag.splitter import child_splitter, parent_splitter
from typing import List
from langchain_core.documents import Document
from utils.config_handler import chroma_config
from model.model_factory import embeddings_model,chat_flash_model
from utils.path_tool import get_abs_path


vectorstore = Chroma(
    collection_name=chroma_config["collection_name"],
    embedding_function=embeddings_model,
    persist_directory=get_abs_path(chroma_config["persist_directory"])
)

# docstore = InMemoryStore()

# 底层redis kv
redis_raw_store = RedisStore(redis_url="redis://localhost:6379", namespace="edu_kb_parent")

# 包装序列化，把Document转bytes、取出再还原Document
docstore = EncoderBackedStore(
    store=redis_raw_store,
    key_encoder=lambda k: k,
    value_serializer=lambda doc: json.dumps(doc.model_dump()).encode("utf-8"),
    value_deserializer=lambda b: Document.model_validate(json.loads(b.decode("utf-8")))
)
retriever = ParentDocumentRetriever(
    vectorstore=vectorstore,
    docstore=docstore,
    child_splitter=child_splitter,
    parent_splitter=parent_splitter,
    search_kwargs={"k": chroma_config["k"]}
)

def add_docs_to_kb(docs: List[Document]):
    retriever.add_documents(docs)

if __name__ == '__main__':
    res = retriever.invoke("上课用什么软件?")
    print(res)