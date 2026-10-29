from abc import ABC, abstractclassmethod
from typing import Optional
from utils.config_handler import rag_config
from langchain_core.embeddings import Embeddings
from langchain_community.chat_models.tongyi import ChatTongyi,BaseChatModel
from langchain_community.embeddings import DashScopeEmbeddings
from dotenv import load_dotenv
load_dotenv(override=True)


class BaseModelFactory(ABC):
    @abstractclassmethod
    def get_model(self) -> Optional[Embeddings | BaseChatModel]:
        pass

class ChatModelFactory(BaseModelFactory):
    def get_model(self) ->  BaseChatModel:
        return ChatTongyi(model=rag_config["chat_model_name"])

class ChatModelFlashFactory(BaseModelFactory):
    def get_model(self) ->  BaseChatModel:
        return ChatTongyi(model=rag_config["model_qwen_flash"])

class EmbeddingsFactory(BaseModelFactory):
    def get_model(self) -> Embeddings:
        return DashScopeEmbeddings(model=rag_config["embedding_model_name"])

chat_model = ChatModelFactory().get_model()
chat_flash_model = ChatModelFlashFactory().get_model()
embeddings_model = EmbeddingsFactory().get_model()