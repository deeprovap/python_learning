from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
credential = AzureCliCredential()
resource_client = ResourceManagementClient(credential,
'bba947d9-81cc-45b7-9309-00bd26b8856d')

#Create resource group
rg = resource_client.resource_groups.create_or_update(
    'dev_resource_group',
   parameters= { 'location' : 'eastus',
    'tags' : {'environment' : 'development','owner' : 'deeprova'}
    }
)

#update tag for existing resource group
rg_update = resource_client.resource_groups.create_or_update(
    resource_group_name= 'test_resource_group',
    parameters= { 'location' : 'eastus',
        'tags' : { 'environment' : 'test','owner' :'David'} })




# create  tag for all resource grp

