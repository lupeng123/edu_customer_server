import asyncio

from fastapi import APIRouter,UploadFile
from rag.loader import load_file
from utils.md5_tool import check_md5,save_md5,get_md5_str
import tempfile
import os
from pathlib import Path
from rag.vector_store import add_docs_to_kb

router = APIRouter(prefix="/api/kb", tags=["kb"])
@router.post("/upload")
async def upload_kb(file: UploadFile):
    try:
        raw_bytes = await file.read()
        text = raw_bytes.decode("utf-8")
        file_name = file.filename
        md5_str = get_md5_str(text)
        if check_md5(md5_str):
            return {"code": -1, "msg": f"{file_name}文件已经存在，请勿重复添加"}

        suffix = Path(file.filename).suffix
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as f:
            f.write(raw_bytes)
            tmp_path = f.name
        docs = load_file(tmp_path)

        await asyncio.to_thread(add_docs_to_kb, docs)
        # add_docs_to_kb(docs)
        os.unlink(tmp_path)

        save_md5(md5_str)
        return {"code": 0, "msg": "入库成功", "doc_count": len(docs)}
    except Exception as e:
        return {"code": -1, "msg": f"入库失败：{str(e)}"}