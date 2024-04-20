from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
credential = AzureCliCredential()
resource_client = ResourceManagementClient(credential,
'bba947d9-81cc-45b7-9309-00bd26b8856d')
rg_list = resource_client.resource_groups.list()
for group in rg_list:
    print(f'{group.name}')

rg_delete = resource_client.resource_groups.begin_delete(
    resource_group_name='dev_resource_group')

rg_delete.wait()

rg_list = resource_client.resource_groups.list()
for group in rg_list:
    print(f'{group.name}')