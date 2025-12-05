from model_security_client.api import ModelSecurityAPIClient
import pprint
import os
from dotenv import load_dotenv

#Load the environmental variable
load_dotenv()
local_uuid = os.getenv("SECURITY_GROUP_UUID_LOCAL")

if __name__ == "__main__":

    # Initialize the client
    client = ModelSecurityAPIClient(
        base_url="https://api.sase.paloaltonetworks.com/aims"
    )

    #Performing the scan
    result = client.scan(
        security_group_uuid=local_uuid,
        model_path="/Users/cekanayake/Documents/ModelScan/my-local-model/wi-gptp/"
    )
    print(f"Scan completed: {result.eval_outcome}\n")
    
    
    try:
        data_dict = result.model_dump()
    except AttributeError:
        data_dict = result.model_dump()
        
    pprint.pprint(data_dict, indent=4)