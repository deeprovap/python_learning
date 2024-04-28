from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from settings import azure_subscription_id

credential = AzureCliCredential()

resource_client = ResourceManagementClient(credential, azure_subscription_id)

# Create resource group
rg = resource_client.resource_groups.create_or_update(
    "dev1_resource_group",
    parameters={
        "location": "eastus",
        "tags": {"environment": "development", "owner": "deeprova"},
    },
)

# update tag for existing resource group
rg_update = resource_client.resource_groups.create_or_update(
    resource_group_name="test_resource_group",
    parameters={
        "location": "eastus",
        "tags": {"environment": "test", "owner": "David"},
    },
)


# create  tag for all resource grp
