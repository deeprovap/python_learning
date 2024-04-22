from azure.identity import AzureCliCredential
from azure.mgmt.storage import StorageManagementClient # type: ignore
credential = AzureCliCredential()
storage_client = StorageManagementClient(credential,
'bba947d9-81cc-45b7-9309-00bd26b8856d')
import random

storage_name_default = 'deeprovatest'



while True:
    storage_name = f'{storage_name_default }{random.randint(1,100)}'

    if not storage_client.storage_accounts.check_name_availability({'name' : storage_name }):
        print(f'The {storage_name} is not available/ trying again.')
    else:
        print(f'creating storage account {storage_name}')
        storage_name_final = storage_client.storage_accounts.begin_create(
    resource_group_name = 'test_resource_group',
    account_name = storage_name,
    parameters = {
        'location' : 'eastus',
        'kind' : 'BlockBlobStorage',
        'sku' :{'name' : 'Premium_LRS'}
        }
        )
        break
