import os
import json

def set_default_cell_type_to_markdown():
    # 获取 JupyterLab 的用户设置目录
    jupyter_config_dir = os.path.join(os.path.expanduser("~"), ".jupyter", "lab", "user-settings", "@jupyterlab", "notebook-extension")
    
    # 创建目录路径
    os.makedirs(jupyter_config_dir, exist_ok=True)
    
    # 设置文件路径
    config_file = os.path.join(jupyter_config_dir, "overrides.json")
    
    # 设置内容
    config_content = {
        "notebook:defaultCellType": "markdown"
    }
    
    # 写入配置文件
    with open(config_file, "w") as f:
        json.dump(config_content, f, indent=4)
    
    print("Default cell type set to Markdown.")

if __name__ == "__main__":
    set_default_cell_type_to_markdown()
