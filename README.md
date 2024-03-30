# DeepInfra image object detector

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Description

This repository showcases an object detector in images using an example model named `yolos-base` by `hustvl` already pre-provided. The example model
uses the DeepInfra backend to detect objects in your images.

## Features

- Fast object detection in images
- Many helper functions for easier use
- Easily add your own models using the same structure.

## Installation

1. Clone the repository.
2. Install the dependencies using `pip install -r requirements.txt` in root
3. Write your code and use the API class to detect objects (elaboration below)

## Usage

Example usage: How to detect objects in an image called "img.jpg"

This is the image:

![example_image](https://i.imgur.com/VquOGsQ.jpeg)

1. Create your python file in the root directory
2. import neccessary modules

You need to import:

- The **API** class

Optional imports:

- Helper Functions
```py
from res.transformers.__helper__ import ...
```

__helper__.py
```py
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
```

- Model information:
```py
# str, str, str | "hustvl/yolos-base", "yolos-base", "hustvl"
from res.transformers.yolos_base import model_path, model, author
```

To import the API class, use:

```py
from res.transformers.yolos_base.transformer import API
```

Next, initialize the API class

```py
API = API()
```

Extract `base64` data from your image

1. Without helper function:

```py
import base64

with open("img.jpg", "rb") as f: # enter your actual image path; i put in my example path.
    image_b64: str = base64.b64encode(f.read()).decode()
```

2. Using helper function:

```py
from res.transformers.__helper__ import img_to_b64

# image here is just a string with the contents 'img.jpg'. It's a path.
image_b64: str = img_to_b64(image)
```

Submit to API's `detect` function.

```py
output = API.detect(image_b64)
```

Output format:

```plain
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

Additional helper functions

```py
print(f"Label: {_parse_label(output)}")
print(f"Box: {_parse_box(output)}")
print(f"Request ID: {_parse_request_id(output)}")
print(f"Runtime: {_parse_runtime(output)}")
print(f"Score: {_parse_score(output)}")
print(f"Status: {_parse_status(output)}")
```

Output:

```plain
Label: person
Box: {'xmin': 0, 'ymin': 0, 'xmax': 300, 'ymax': 297}
Request ID: RgVuNHcSRvPg2VH7MUNprYoS
Runtime: 143
Score: 0.99928218126297
Status: succeeded
```

## Legal notice

Please refer to the [Legal Notice](LEGAL.md)

## License

This project is licensed under the [MIT License](LICENSE.md).
