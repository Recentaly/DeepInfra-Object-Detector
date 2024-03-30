from res.transformers.yolos_base.transformer import API
from res.transformers.yolos_base import model_path, model, author

from res.transformers.__helper__ import img_to_b64, _parse_box, _parse_label, _parse_request_id, _parse_runtime, _parse_score, _parse_status, get_user_agent, get_random_number, generate_random_id, get_timestamp, get_uuid

# Initialize the API
API = API()

# Print the model information
print(f"Model: {model} by {author}. Model path: {model_path}")

print(f"Using version: {API._get_version()}")

# Detect objects in an image
image = "img.jpg"
image_b64 = img_to_b64(image)

# Parse the output
output = API.detect(image_b64)
print(f"Label: {_parse_label(output)}")
print(f"Box: {_parse_box(output)}")
print(f"Request ID: {_parse_request_id(output)}")
print(f"Runtime: {_parse_runtime(output)}")
print(f"Score: {_parse_score(output)}")
print(f"Status: {_parse_status(output)}")
