import random
import time
from azure.identity import AzureCliCredential
from azure.mgmt.storage import StorageManagementClient
from azure.storage.blob import BlobClient, BlobServiceClient,ContainerClient
from settings import azure_subscription_id, default_location

credential = AzureCliCredential()
storage_client = StorageManagementClient(credential,azure_subscription_id)


STORAGE_NAME_DEFAULT = 'deeprovatest'
CONTAINER_DEFAULT_NAME = 'file'
storage_name = f'{STORAGE_NAME_DEFAULT}{random.randint(1,100)}'

while True:
    if not storage_client.storage_accounts.check_name_availability(
        {"name": storage_name}
    ):
        print(f'{storage_name} is not avaialable. Checking a new one.')
    else:
        print(f'creating storage {storage_name}')
        storage_name_final = storage_client.storage_accounts.begin_create(
            resource_group_name= 'test_resource_group',
            account_name= storage_name,
            parameters={
                'location' : default_location,
                'kind' : 'BlockBlobStorage',
                'sku': {'name' : 'Premium_LRS'},
            },
        
        )
        break

#Checking if storage account is created successfully
while True:
      if storage_name.provisioning_state == "Succeeded":
            print("Storage account creation successful!")
            break
      else:
            print("Waiting for storage account to be provisioned...")
            time.sleep(10) 

# Get the storage account key
storage_keys = storage_client.storage_accounts.list_keys('test_resource_group', storage_name)
storage_key = storage_keys.keys[0].value

# Build the storage connection string
storage_connection_string = f"DefaultEndpointsProtocol=https;AccountName={storage_name};AccountKey={storage_key};EndpointSuffix=core.windows.net"

Blob_service_clent = BlobServiceClient.from_connection_string(storage_connection_string)
container_name = f'{CONTAINER_DEFAULT_NAME}{random.randint(1,100)}'
while True:
        container_client = Blob_service_clent.get_container_client(container_name)
        if container_client.exists():
             print(f'{container_name} is not available. Checking for a new one.')

        else:
             print(f'creating container {container_name}')
             container_name_final = storage_client.blob.containers.create(
                  resource_group_name= 'test_resource_group',
                  account_name= storage_name,
                  container_name = container_name,
                  blob_container ={}
        )
        break
