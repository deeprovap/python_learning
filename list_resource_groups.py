from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
credential = AzureCliCredential()
resource_client = ResourceManagementClient(credential,
'bba947d9-81cc-45b7-9309-00bd26b8856d')
#list all resorce group 

rg_list = resource_client.resource_groups.list()
for group in rg_list:
    print(f'{group.name}: {group.location}: {group.tags}')

#list all resorce group with a specific filter
tag_key = 'owner'
tag_value = 'deeprova'
filtered_list = resource_client.resource_groups.list(filter=f"tagName eq '{tag_key}' and tagValue eq '{tag_value}'")
for gr in filtered_list:
    print(gr.name)