import yaml
from utils.path_tool import get_abs_path

def get_rag_config(config_path:str=get_abs_path("config/rag.yml"),encoding:str="utf-8"):
    with open(config_path,"r",encoding=encoding) as f:
        return yaml.load(f,Loader=yaml.FullLoader)

def get_agent_config(config_path:str=get_abs_path("config/agent.yml"),encoding:str="utf-8"):
    with open(config_path,"r",encoding=encoding) as f:
        return yaml.load(f,Loader=yaml.FullLoader)

def get_chroma_config(config_path:str=get_abs_path("config/chroma.yml"),encoding:str="utf-8"):
    with open(config_path,"r",encoding=encoding) as f:
        return yaml.load(f,Loader=yaml.FullLoader)

def get_prompt_config(config_path:str=get_abs_path("config/prompt.yml"),encoding:str="utf-8"):
    with open(config_path,"r",encoding=encoding) as f:
        return yaml.load(f,Loader=yaml.FullLoader)

rag_config = get_rag_config()
agent_config = get_agent_config()
chroma_config = get_chroma_config()
prompt_config = get_prompt_config()

if __name__ == '__main__':
    print(prompt_config["main_prompt_path"])
    print(prompt_config["report_prompt_path"])

