# 校验md5是否存在
import os
from utils.config_handler import chroma_config
from utils.path_tool import get_abs_path
import hashlib


# 校验md5是否存在
def check_md5(md5_str:str):
    if not os.path.exists(get_abs_path(chroma_config["md5_hex_store"])):
        open(get_abs_path(chroma_config["md5_hex_store"]), "w", encoding="utf-8").close()
        return False
    with open(get_abs_path(chroma_config["md5_hex_store"]), "r", encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip()
            if line == md5_str:
                return True
    return False


# 保存md5
def save_md5(md5_str:str):
    with open(get_abs_path(chroma_config["md5_hex_store"]), 'a',encoding="utf-8") as f:
        f.write(md5_str+"\n")


# 获取md5
def get_md5_str(input_str:str):
    str_bytes = input_str.encode('utf-8')
    # 创建md5对象
    md5_obj = hashlib.md5()  # 得到md5对象
    md5_obj.update(str_bytes)  # 更新内容（传入即将要转换的字节数组）
    md5_hex = md5_obj.hexdigest()  # 得到md5的十六进制字符串

    return md5_hex