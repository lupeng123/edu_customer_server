import asyncio
import json

from sse_starlette.sse import EventSourceResponse
from fastapi import APIRouter
from langchain_community.chat_message_histories import SQLChatMessageHistory
from agent.react_agent import ReactAgent

router = APIRouter(prefix="/api/chat", tags=["chat"])
react_agent = ReactAgent()

# def get_session_history(session_id: str):
#     return SQLChatMessageHistory(session_id, connection=SQL_HISTORY_DB)

@router.get("/stream")
async def chat_stream(session_id: str, query: str):
    async def sse_generator():
        try:
            res = await react_agent.ainvoke_message(query=query, session_id=session_id)
            for c in res:
                await asyncio.sleep(0.05)
                yield {"event": "token", "data": c}
            yield {"event": "end","data": ""}
        except Exception as e:
            yield {"event": "error", "data": json.dumps({"error": str(e)}, ensure_ascii=False)}

    return EventSourceResponse(sse_generator())
