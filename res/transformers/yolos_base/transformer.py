"""
The transformer class for the Yolos Base transformer.
"""

import requests

from . import get_version
from .. import get_user_agent, get_random_number
from ...Typing import *

class API(object):

    """
    The API class for the Yolos Base transformer.
    """

    def __init__(self) -> None:

        """
        The API class for the Yolos Base transformer."""
        
        self.__version: str = get_version()

    def _get_version(self) -> str:

        """
        Get the version of the Yolos Base transformer.
        """

        return self.__version
    
    def detect(self, image: B64_Image | str) -> JSON:

        """
        Detect objects in an image.

        :param image: The image to detect objects in.

        :return: The detected objects.

        Output format:

        ```json
        {
            "request_id": "xxxxxxxxxxxxxxxxxxxxxxxx" (length 24),
            "inference_status": {
                "status": "succeeded",
                "runtime_ms": x (int),
                "cost": 0, (int),
                "tokens_generated": None (null),
                "tokens_input": None (null)
            },
            "results": [
                {
                    "label": "xxxx", (str),
                    "score": 0.xxxx, (float),
                    "box": {
                        "xmin": x (int),
                        "ymin": x (int),
                        "xmax": x (int),
                        "ymax": x (int)
                }
            ]
        }
        ```
        """

        __headers = {
            "Host": "api.deepinfra.com",
            "User-Agent": f"{get_user_agent()}",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json",
            "Content-Length": f"{get_random_number(30_000, 50_000)}",
            "Origin": "https://deepinfra.com",
            "Connection": "keep-alive",
            "Referer": "https://deepinfra.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
        }

        __data = {
            "image": image
        }

        response = requests.post(
            f"https://api.deepinfra.com/v1/inference/hustvl/yolos-base?version={self.__version}",
            headers=__headers,
            json=__data
        )
        response.raise_for_status()

        return response.json()

