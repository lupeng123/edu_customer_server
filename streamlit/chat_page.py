import streamlit as st
import sseclient
import requests

st.set_page_config(page_title="客服对话调试", layout="wide")
st.title("💬 培优学堂客服RAG调试台")

API_BASE = "http://127.0.0.1:8000/api/chat/stream"

# 初始化session
if "messages" not in st.session_state:
    st.session_state.messages = []
if "session_id" not in st.session_state:
    st.session_state.session_id = "user_001"

with st.sidebar:
    st.header("会话配置")
    st.session_state.session_id = st.text_input("session_id", value=st.session_state.session_id)
    if st.button("🗑️ 清空当前页面对话历史"):
        st.session_state.messages = []
        st.rerun()

# 渲染历史消息
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("请输入家长咨询问题...")

if user_input:
    # 用户消息入页面历史
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # 流式占位
    with st.chat_message("assistant"):
        full_response = ""
        resp_placeholder = st.empty()
        with st.spinner("AI思考中。。。"):
            params = {
                "session_id": st.session_state.session_id,
                "query": user_input
            }
            try:
                stream_resp = requests.get(API_BASE, params=params, stream=True)
                client = sseclient.SSEClient(stream_resp)
                for event in client.events():
                    if event.event == "token":
                        full_response += event.data
                    elif event.event == "end":
                        break
                    elif event.event == "error":
                        full_response += "\n【服务异常】" + event.data

                    resp_placeholder.write(full_response)
            except Exception as e:
                full_response = f"请求失败：{str(e)}"
                st.chat_message("assistant").write(full_response)

        st.session_state.messages.append({"role": "assistant", "content": full_response})

