from utils.path_tool import get_abs_path
from utils.config_handler import prompt_config
from utils.logger import logger


def load_system_prompt():
    try:
        path = get_abs_path(prompt_config["main_prompt_path"])
    except KeyError as e:
        logger.error("提示词配置文件中没有main_prompt_path")
        raise e

    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        logger.error(f"[load_system_prompts]解析系统提示词出错，{str(e)}")
        raise e

def load_rag_prompt():
    try:
        path = get_abs_path(prompt_config["rag_summarize_prompt_path"])
    except KeyError as e:
        logger.error("提示词配置文件中没有rag_summarize_prompt_path")
        raise e

    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        logger.error(f"[load_rag_prompt]解析系统提示词出错，{str(e)}")
        raise e

def load_rag_extract_prompt():
    try:
        path = get_abs_path(prompt_config["rag_extract_prompt_path"])
    except KeyError as e:
        logger.error("提示词配置文件中没有rag_extract_prompt_path")
        raise e

    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        logger.error(f"[load_rag_prompt]解析系统提示词出错，{str(e)}")
        raise e

def load_report_prompt():
    try:
        path = get_abs_path(prompt_config["report_prompt_path"])
    except KeyError as e:
        logger.error("提示词配置文件中没有report_prompt_path")
        raise e

    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        logger.error(f"[load_report_prompts]解析系统提示词出错，{str(e)}")
        raise e

if __name__ == '__main__':
    print(load_report_prompt())