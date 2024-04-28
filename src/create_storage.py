from azure.identity import AzureCliCredential
from azure.mgmt.storage import StorageManagementClient
from settings import azure_subscription_id

credential = AzureCliCredential()
storage_client = StorageManagementClient(credential, azure_subscription_id)

storage_name = storage_client.storage_accounts.begin_create(
    resource_group_name="test_resource_group",
    account_name="deeprovatest01",
    parameters={
        "location": "eastus",
        "kind": "BlockBlobStorage",
        "sku": {"name": "Premium_LRS"},
    },
)
