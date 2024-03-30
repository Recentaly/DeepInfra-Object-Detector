"""
Helper functions for transformers
"""

# -------------------------------------------- IMPORTS -------------------------------------------- #
import secrets
import base64
import random
import string
import time

from fake_useragent import UserAgent
from uuid import uuid4

from ..Typing import *

# -------------------------------------------- GENERATION RELATED -------------------------------------------- #
def img_to_b64(image: Image) -> B64_Image:
          
        """
        Convert an image to a base64 string.

        :param image: The image to convert to a base64 string.

        :return: The base64 string.
        """
    
        with open(image, "rb") as f:
            return base64.b64encode(f.read()).decode()

# -------------------------------------------- QUICK-ACCESS RELATED -------------------------------------------- #
def generate_random_id(length: int) -> str:

    """
    Generate a random ID of a given length.

    :param length: The length of the random ID.

    :return: The random ID.
    """
    
    # Define the characters to choose from
    characters = string.ascii_letters + string.digits
    
    # Generate a random ID by randomly selecting characters from the defined set
    random_id = ''.join(random.choice(characters) for _ in range(length))
    
    return random_id

def get_timestamp() -> int:

    """
    Get the current timestamp.

    :return: The current timestamp.
    """

    return int(time.time() * 1000)

def get_user_agent() -> str:
    
    """
    Get a random user agent.
    """
    
    return UserAgent().random

def get_uuid() -> str:
    
    """
    Get a random UUID version 4.

    :return: The UUID.
    """
    
    return str(uuid4())

def get_random_number(min: int, max: int) -> int:
      
    """
    Get a random number.

    :param min: The minimum number.
    :param max: The maximum number.

    :return: The random number.
    """
  
    return secrets.randbelow(max) + min

# -------------------------------------------- OUTPUT RELATED -------------------------------------------- #
def _parse_label(output: JSON) -> str:

    """
    Parse the label from the output.

    :param output: The output from the `detect` function to parse the label from.

    :return: The label. (str) (example="person")
    """

    try:    return output["results"][0]["label"]
    except: return None

def _parse_runtime(output: JSON) -> int:

    """
    Parse the runtime from the output.

    :param output: The output from the `detect` function to parse the runtime from.

    :return: The runtime. (int) (example=100)
    """

    try:    return output["inference_status"]["runtime_ms"]
    except: return None

def _parse_score(output: JSON) -> float:
    
    """
    Parse the score from the output.
    
    :param output: The output from the `detect` function to parse the score from.
    
    :return: The score. (float) (example=0.99)
    """
    
    try:    return output["results"][0]["score"]
    except: return None

def _parse_box(output: JSON) -> Dict[str, int]:
        
    """
    Parse the box from the output.
        
    :param output: The output from the `detect` function to parse the box from.
        
    :return: The box. (dict) (example={"xmin": 0, "ymin": 0, "xmax": 100, "ymax": 100})
    """
        
    try:    return output["results"][0]["box"]
    except: return None

def _parse_request_id(output: JSON) -> str:
        
    """
    Parse the request ID from the output.
    
    :param output: The output from the `detect` function to parse the request ID from.
    
    :return: The request ID. (str) (example="xxxxxxxxxxxxxxxxxxxxxxxx")
    """
    
    try:    return output["request_id"]
    except: return None

def _parse_status(output: JSON) -> str:
        
    """
    Parse the status from the output.
        
    :param output: The output from the `detect` function to parse the status from.
        
    :return: The status. (str) (example="succeeded")
    """
        
    try:    return output["inference_status"]["status"]
    except: return None

# -------------------------------------------- MODULE EXPORTS -------------------------------------------- #
__all__ = [
    'generate_random_id',
    'get_timestamp',
    'get_user_agent',
    'get_uuid',
    'img_to_b64',
    'get_random_number',
    '_parse_label',
    '_parse_runtime',
    '_parse_score',
    '_parse_box',
    '_parse_request_id',
    '_parse_status'
]