from langchain_text_splitters import RecursiveCharacterTextSplitter
from utils.config_handler import chroma_config

# 子块：用于向量化检索
child_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chroma_config["child_chunk_size"],
    chunk_overlap=chroma_config["child_chunk_overlap"],
    separators=chroma_config["child_separators"]
)
# 父块：返回完整上下文
parent_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chroma_config["parent_chunk_size"],
    chunk_overlap=chroma_config["parent_chunk_overlap"],
    separators=chroma_config["parent_separators"]
)
