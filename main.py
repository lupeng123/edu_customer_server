from fastapi import FastAPI
from api.kb_api import router as kb_router
from api.chat_stream import router as chat_router

app = FastAPI(title="培优学堂课程客服RAG服务")
# app.include_router(chat_router, prefix="/api")
app.include_router(kb_router)
app.include_router(chat_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
