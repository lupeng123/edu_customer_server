# 培优学堂课程客服RAG服务
> 基于 langchain LangGraph Rag Agent 的检索增强知识库问答系统

## ✨ 项目简介
本项目是一套具备工具调用能力的 RAG 智能问答应用，支持 文档上传入库、文档切片、向量检索、Agent 自主决策、多轮对话持久化记忆。
使用 FastAPI 搭建后端流式接口，Streamlit 作为交互前端，适合企业内部文档答疑、课程资料咨询、私有知识库落地场景。

## 🧩 技术栈
- Python 3.11
- 环境配置：miniconda,docker
- Web 服务：FastAPI、Uvicorn、sse-starlette（SSE流式输出）
- 大模型：qwen-max,text-embedding-v4,qwen-flash
- Agent & 记忆：LangGraph + Checkpointer（InMemorySaver内存级存储）
- RAG 模块：LangChain、ChromaDB、ParentDocumentRetriever、redis
- 中间件：SummarizationMiddleware(历史消息摘要)
- 分片：RecursiveCharacterTextSplitter
- 前端：Streamlit
- 向量库：chroma(正式服可切换milvus)
- 记忆存储：InMemorySaver(正式服可切换PostgreSQL)

## 🎯 核心功能
1. 📄 文件上传，自动分块并向量化存入向量库
2. 🔍 Agent 智能路由，自主判断是否需要检索知识库，降低幻觉
3. 💬 多轮上下文记忆，LangGraph Checkpointer 保存对话状态快照
4. ⚡ SSE 流式输出，前端实现打字机展示效果
6. 📌 使用SummarizationMiddleware对历史消息进行摘要
7. 🧠 支持 ParentDocumentRetriever 父子文档检索方案，优化召回效果


## 运行
1. 安装依赖 pip install -r requirements.txt
1. 运行main文件
2. streamlit run kb_upload.py   进入文件上传页面上传edu_text目录下的知识库文档
3. streamlit run chat_page.py   进入客服页面

