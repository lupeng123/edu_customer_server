import os


def get_prorect_root() -> str:
    current_file_path = os.path.abspath(__file__)
    current_dir = os.path.dirname(current_file_path)
    project_root = os.path.dirname(current_dir)
    return project_root

# 传文件相对路径返回绝对路径
def get_abs_path(relative_path:str) -> str:
    return os.path.join(get_prorect_root(), relative_path)
