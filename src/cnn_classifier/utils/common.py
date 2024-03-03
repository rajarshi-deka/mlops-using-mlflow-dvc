# Import libraries
import base64
import joblib
import json
import os
import yaml
from box import ConfigBox
from box.exceptions import BoxValueError    # For handling exceptions
from cnn_classifier import logger
from ensure import ensure_annotations
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(yaml_path:Path) -> ConfigBox:
    '''
        Function to read YAML files and then return the content
        Args:
            path_to_yaml (Path): YAML file path
        Raises:
            ValueError: If YAML file is empty
            e: Empty file
        Returns:
            ConfigBox: ConfigBox type
    '''
    try:
        with open(yaml_path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file : {yaml_file} loaded successfully!!!")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(dir_path_list:list, verbose=True):
    '''
        Function to create list of directories
        Args:
            dir_path (list): List of directory path
            ignore_log (bool, optional): Ignore if mutiple directories are to be created. Defaults to False
    '''
    for path in dir_path_list:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}") 

@ensure_annotations
def save_json(path:Path, json_data:dict):
    '''
        Function to save JSON data
        Args:
            path (Path): Path to store JSON data
            json_data (dict): Data to be saved in JSON file
    '''
    with open(path, "w") as file:
        json.dump(json_data, file, indent=4)
    logger.info(f"JSON file saved at: {path}")

@ensure_annotations
def load_json(json_path:Path) -> ConfigBox:
    '''
        Function to load JSON files
        Args:
            json_path (Path): JSON file path
        Returns:
            ConfigBox: Data as class attributes instead of dict
    '''
    with open(json_path) as file:
        content = json.load(file)
    logger.info(f"JSON file loaded successfully from: {json_path}")
    return ConfigBox(content)

@ensure_annotations
def save_binary(data:Any, path:Path):
    '''
        Function to save binary file
        Args:
            data (Any): Data to be saved as binary
            path (Path): Path to store binary file
    '''
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_binary(binary_path:Path) -> Any:
    '''
        Function to load binary data
        Args:
            binary_path (Path): Binary file path
        Returns:
            Any: Object stored in the file
    '''
    data = joblib.load(binary_path)
    logger.info(f"Binary file loaded from: {binary_path}")
    return data

@ensure_annotations
def get_size(file_path:Path) -> str:
    '''
        Function to get file size in KB
        Args:
            file_path (Path): File path
        Returns:
            str: Size in KB
    '''
    size_in_kb = round(os.path.getsize(file_path)/1024)
    return f"~ {size_in_kb} KB"

def encode_image(image_path):
    '''
        Function to encode an image to Base64 encoding        
    '''
    with open(image_path, "rb") as file:
        return base64.b64encode(file.read())
    
def decode_image(encoded_image, file_name):
    '''
        Function to decode an encoded image and save it as a file        
    '''
    image_data = base64.b64decode(encoded_image)
    with open(file_name, "wb") as file:
        file.write(image_data)
        file.close()
        logger.info(f"Image successfully saved as: {file_name}")


    