from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from settings import azure_subscription_id

credential = AzureCliCredential()
resource_client = ResourceManagementClient(credential, azure_subscription_id)
rg_list = resource_client.resource_groups.list()
for group in rg_list:
    print(f"{group.name}")

rg_delete = resource_client.resource_groups.begin_delete(
    resource_group_name="dev_resource_group"
)

rg_delete.wait()

rg_list = resource_client.resource_groups.list()
for group in rg_list:
    print(f"{group.name}")
