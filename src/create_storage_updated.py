"""this is to update or create storage"""

import random
from azure.identity import AzureCliCredential
from azure.mgmt.storage import StorageManagementClient
from settings import azure_subscription_id, default_location

credential = AzureCliCredential()
storage_client = StorageManagementClient(credential, azure_subscription_id)
STORAGE_NAME_DEFAULT = "deeprovatest"

while True:
    storage_name = f"{STORAGE_NAME_DEFAULT}{random.randint(1,100)}"

    if not storage_client.storage_accounts.check_name_availability(
        {"name": storage_name}
    ):
        print(f"The {storage_name} is not available/ trying again.")
    else:
        print(f"creating storage account {storage_name}")
        storage_name_final = storage_client.storage_accounts.begin_create(
            resource_group_name="test_resource_group",
            account_name=storage_name,
            parameters={
                "location": default_location,
                "kind": "BlockBlobStorage",
                "sku": {"name": "Premium_LRS"},
            },
        )
        break
