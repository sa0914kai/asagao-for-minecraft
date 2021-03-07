import os

# required
DISCORD_TOKEN = os.environ.get('DISCORD_TOKEN')
CONOHA_API_TENANT_ID = os.environ.get('CONOHA_API_TENANT_ID')
CONOHA_API_IDENTITY_SERVICE = os.environ.get('CONOHA_API_IDENTITY_SERVICE')
CONOHA_API_USER_NAME = os.environ.get('CONOHA_API_USER_NAME')
CONOHA_API_USER_PASSWORD = os.environ.get('CONOHA_API_USER_PASSWORD')

CONOHA_API_IMAGE_SERVICE = os.environ.get('CONOHA_API_IMAGE_SERVICE')
CONOHA_API_COMPUTE_SERVICE = os.environ.get('CONOHA_API_COMPUTE_SERVICE')
CONOHA_API_NETWORK_SERVICE = os.environ.get('CONOHA_API_NETWORK_SERVICE')
CONOHA_API_VM_PLAN_FLAVOR_UUID = os.environ.get('CONOHA_API_VM_PLAN_FLAVOR_UUID')


# option
VM_AND_IMAGE_NAME = 'asagao-for-minecraft-'+os.environ.get('VM_AND_IMAGE_NAME', '') if os.environ.get('VM_AND_IMAGE_NAME', '') != '' else 'asagao-for-minecraft'
ADMIN_USER_ID = f"<@{os.environ.get('ADMIN_USER_ID', '')}>" if os.environ.get('ADMIN_USER_ID', '') != '' else ''
