# Import libraries
import os
import logging
from pathlib import Path

# Initialize logger
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# Define project name
project_name = "cnn_classifier"

# Define the list of files to be added in the repository
list_of_files = [
    ".github/workflow/.gitkeep",    # Required for CI/CD deployment
    f"src/{project_name}/__init__.py",  # Constructor file to create 'cnn_classifier' folder as a local package
    f"src/{project_name}/components/__init__.py",   # Constructor file to create 'components' folder as a local package
    f"src/{project_name}/utils/__init__.py",    # Constructor file to create 'utils' folder as a local package
    f"src/{project_name}/config/__init__.py",   # Constructor file to create 'config' folder as a local package 
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py", # Constructor file to create 'pipeline' folder as a local package 
    f"src/{project_name}/entity/__init__.py" ,  # Constructor file to create 'entity' folder as a local package
    f"src/{project_name}/constants/__init__.py",    # Constructor file to create 'constants' folder as a local package
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",    # Notebook file to carry out experiments
    "templates/index.html"  # Code for creating the UI of the project
]

# Python script to create the above folder structure along with the list_of_file
for filepath in list_of_files:
    filepath = Path(filepath)
    file_dir, file_name = os.path.split(filepath)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Created directory: {file_dir} for the file: {file_name}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as file:
            pass
            file.close()
            logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"{filepath} already exists")
