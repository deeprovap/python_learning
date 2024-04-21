from azure.identity import AzureCliCredential
from azure.mgmt.storage import StorageManagementClient # type: ignore
credential = AzureCliCredential()
storage_client = StorageManagementClient(credential,
'bba947d9-81cc-45b7-9309-00bd26b8856d')

storage_name = storage_client.storage_accounts.begin_create(
    resource_group_name = 'test_resource_group',
    account_name = 'deeprovatest01',
    parameters = {
        'location' : 'eastus',
        'kind' : 'BlockBlobStorage',
        'sku' :{'name' : 'Premium_LRS'}
        }
        )