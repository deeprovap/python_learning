import os
from dotenv import load_dotenv
load_dotenv()
azure_subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
azure_storage_access_key = os.getenv("AZURE_STORAGE_ACCESS_KEY")
default_location = "eastus"
