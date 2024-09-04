import os
import json

def set_default_cell_type_to_markdown():
    # Get the JupyterLab configuration directory
    jupyter_config_dir = os.path.join(os.path.expanduser("~"), ".jupyter", "lab", "user-settings", "@jupyterlab", "notebook-extension")
    print("JupyterLab configuration directory:", jupyter_config_dir)

    # Create the directory if it does not exist
    if not os.path.exists(jupyter_config_dir):
        print("Creating the JupyterLab configuration directory.")
    else:
        print("JupyterLab configuration directory already exists.")
    os.makedirs(jupyter_config_dir, exist_ok=True)
    
    # Set the path to the configuration file
    config_file = os.path.join(jupyter_config_dir, "overrides.json")
    print("Configuration file:", config_file)
    
    # Set the content of the configuration file
    config_content = {
        "notebook:defaultCellType": "markdown"
    }
    
    # Write the configuration file
    with open(config_file, "w") as f:
        json.dump(config_content, f, indent=4)
    
    print("Default cell type set to Markdown.")

if __name__ == "__main__":
    set_default_cell_type_to_markdown()
