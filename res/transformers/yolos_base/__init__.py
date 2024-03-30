"""
Yolos base transformer specific functions.
"""

from .. import generate_random_id, get_user_agent, get_timestamp, get_uuid, get_random_number

import requests

# variable initialization
model_path: str = "hustvl/yolos-base"
model: str = "yolos-base"
author: str = "hustvl"

def get_version() -> str:
    
    """
    Get the version of the Yolos Base transformer by DeepInfra
    """

    __headers = {
        "Host": "deepinfra.com",
        "User-Agent": f"{get_user_agent()}",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://deepinfra.com/hustvl/yolos-base",
        "purpose": "prefetch",
        "x-nextjs-data": "1",
        "sentry-trace": f"{generate_random_id(32)}-{generate_random_id(16)}-0",
        "baggage": "sentry-environment=production,sentry-release=_Ts4lH7mEEjYhYWZwbaZb,sentry-public_key=f801c69f50c0df3c23ec54c97b396c6f,sentry-trace_id=ad24721a0bfd459a8c65347b60031bbf,sentry-sample_rate=0.001,sentry-transaction=%2F%5B...model_path%5D,sentry-sampled=false",
        "Alt-Used": "deepinfra.com",
        "Connection": "keep-alive",
        "Cookie": "ko_id=" + get_uuid() + "; ko_sid={%22id%22:%221711806286004%22%2C%22lastTouched%22:" + str(get_timestamp) + "}",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers"
    }

    response = requests.get(
        "https://deepinfra.com/_next/data/_Ts4lH7mEEjYhYWZwbaZb/hustvl/yolos-base/api.json?model_path=hustvl&model_path=yolos-base&model_path=api",
        headers=__headers
    )
    response.raise_for_status()

    return str(response.json()["pageProps"]["static_info"]["version"])

__all__ = [
    'generate_random_id',
    'get_user_agent',
    'get_timestamp',
    'get_uuid',
    'get_random_number',
    'model_path',
    'model',
    'author'
]

