from typing import Callable
from langchain.agents import AgentState
from langchain.agents.middleware import before_model, dynamic_prompt, ModelRequest, wrap_tool_call
from langchain_core.messages import ToolMessage
from langgraph.prebuilt.tool_node import ToolCallRequest
from langgraph.runtime import Runtime
from langgraph.types import Command
from utils.logger import logger
from langchain.agents.middleware import SummarizationMiddleware
from model.model_factory import chat_flash_model

@before_model
def log_before_model(state:AgentState,runtime:Runtime) -> None:
    logger.info(f"[log_befor_model]:即将调用模型，带有{len(state['messages'])}条消息")

    logger.debug(f"[log_befor_model]:{type(state['messages'][-1]).__name__} | {state['messages'][-1].content.strip()}")

    return None

@wrap_tool_call
async def monitor_tool(
        request:ToolCallRequest,
        handler:Callable[[ToolCallRequest], ToolMessage | Command],):
    logger.info(f"[tool monitor]执行工具：{request.tool_call['name']}")
    # logger.info(f"[tool monitor]传入参数：{request.tool_call['args']}")

    return await handler(request)

# 历史消息摘要中间件
summarization_middleware = SummarizationMiddleware(
            model=chat_flash_model,
            trigger=[
                ("tokens", 1000),  # 超过 100 tokens 就摘要
            ],
            keep=("messages", 4),
            summary_prompt="对历史消息摘要，消息列表如下\n{messages}",

        )

middlewares = [log_before_model,monitor_tool,summarization_middleware]


