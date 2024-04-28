from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from settings import azure_subscription_id

credential = AzureCliCredential()
resource_client = ResourceManagementClient(credential, azure_subscription_id)
# list all resorce group

rg_list = resource_client.resource_groups.list()
for group in rg_list:
    print(f"{group.name}: {group.location}: {group.tags}")

# list all resorce group with a specific filter
tag_key = "owner"
tag_value = "deeprova"
filtered_list = resource_client.resource_groups.list(
    filter=f"tagName eq '{tag_key}' and tagValue eq '{tag_value}'"
)
for gr in filtered_list:
    print(gr.name)
