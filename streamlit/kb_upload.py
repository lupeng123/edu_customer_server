import streamlit as st
import requests

st.set_page_config(page_title="知识库上传", layout="wide")
st.title("📚 培优学堂 - 知识库文档上传")
st.caption("支持 txt / pdf，上传后自动入库到Chroma向量库")

API_URL = "http://127.0.0.1:8000/api/kb/upload"

uploaded_file = st.file_uploader("选择文档", type=["txt", "pdf"])

if uploaded_file is not None:
    st.info(f"已选择文件：{uploaded_file.name}")
    if st.button("✅ 提交入库"):
        with st.spinner("正在解析文档、切片、入库..."):
            files = {
                "file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)
            }
            resp = requests.post(API_URL, files=files)
            res = resp.json()
            if res.get("code") == 0:
                st.success(f"入库成功！文档数量：{res['doc_count']}")
            else:
                st.error(f"入库失败：{res.get('msg')}")
