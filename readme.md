# AIRS Model Scanning Python SDK

This repository contains a Python SDK implementation for **Palo Alto Networks AI Model Security**. It allows you to programmatically scan AI models (hosted on Hugging Face or stored locally) for vulnerabilities, malicious code, and integrity issues.

Reference https://docs.paloaltonetworks.com/ai-runtime-security/ai-model-security/model-security-to-secure-your-ai-models

## Prerequisites

- **Python 3.12+**
- **pip** (Python package manager)
- A valid **Palo Alto Networks AI Security** account with credentials

## Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/chinthakaek/airs-model-scanning-python-sdk.git](https://github.com/chinthakaek/airs-model-scanning-python-sdk.git)
   cd airs-model-scanning-python-sdk

2. Copy the content of "example env file" and create new .env file. Update with your credentials
    ```bash
    MODEL_SECURITY_CLIENT_ID="your_client_id_here"
    MODEL_SECURITY_CLIENT_SECRET="your_client_secret_here"
    TSG_ID="your_tsg_id_here"
    MODEL_SECURITY_API_ENDPOINT="https://api.sase.paloaltonetworks.com/aims"
    SECURITY_GROUP_UUID_HF="your_huggingface_uuid"
    SECURITY_GROUP_UUID_LOCAL="your_local_uuid"

3. Allow executable Permissions and set the environment
    ```bash
    chmod +x *.sh
    chmod +x *.py
    ./set_envrionment.sh

4. Access the VENV created
    ```bash
    source venv/bin/activate

5. Run the scans
    ```bash
    python3 hf-scan.py https://huggingface.co/AUTOMATIC/promptgen-majinai-unsafe
    or
    python3 local-scan.py /Users/name/models/my-model