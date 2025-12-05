import os
from model_security_client.api import ModelSecurityAPIClient
from dotenv import load_dotenv
import pprint

#Load the environmental variable
load_dotenv()
hf_uuid = os.getenv("SECURITY_GROUP_UUID_HF")

# Initialize the client
client = ModelSecurityAPIClient(
    base_url="https://api.sase.paloaltonetworks.com/aims"
)

result = client.scan(
    security_group_uuid=hf_uuid,
    model_uri="https://huggingface.co/AUTOMATIC/promptgen-majinai-unsafe",
)
print(f"Scan completed: {result.eval_outcome}")
try:
    data_dict = result.model_dump()
except AttributeError:
    data_dict = result.model_dump()
pprint.pprint(data_dict, indent=4)
