"""
Type hints for transformers.
"""

from typing import Any, Dict, List, NewType

B64_Image = NewType("B64_Image", str)
JSON = Dict[str, Any]
Image = NewType("Image", str)

__all__ = [
    'B64_Image',
    'Dict',
    'List',
    'Any',
    'JSON',
    'Image'
]