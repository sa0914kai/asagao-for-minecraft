import os
import json


# Fixed value
VERSION = '0.1.2'


# use environment var in os
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
ADMIN_USER_ID = os.environ.get('ADMIN_USER_ID', '')
DISCORD_CHANNEL_NAMES = os.environ.get('DISCORD_CHANNEL_NAMES', 'minecraft, minecraft-test').replace(' ', '').split(',')

# secret
HOUR_FOR_IMAGE_LEAVE_ALONE_LONG_TIME = os.environ.get('HOUR_FOR_IMAGE_LEAVE_ALONE_LONG_TIME', None)
ALLOW_PROCESS_KILL_COMMAND = os.environ.get('ALLOW_PROCESS_KILL_COMMAND', None)



# use environment var in json file
if os.path.exists('env.json'):
  with open('env.json', 'r') as json_file:
    json = json.load(json_file)

    # required
    DISCORD_TOKEN = json['DISCORD_TOKEN']
    CONOHA_API_TENANT_ID = json['CONOHA_API_TENANT_ID']
    CONOHA_API_IDENTITY_SERVICE = json['CONOHA_API_IDENTITY_SERVICE']
    CONOHA_API_USER_NAME = json['CONOHA_API_USER_NAME']
    CONOHA_API_USER_PASSWORD = json['CONOHA_API_USER_PASSWORD']

    CONOHA_API_IMAGE_SERVICE = json['CONOHA_API_IMAGE_SERVICE']
    CONOHA_API_COMPUTE_SERVICE = json['CONOHA_API_COMPUTE_SERVICE']
    CONOHA_API_NETWORK_SERVICE = json['CONOHA_API_NETWORK_SERVICE']
    CONOHA_API_VM_PLAN_FLAVOR_UUID = json['CONOHA_API_VM_PLAN_FLAVOR_UUID']

    # option
    VM_AND_IMAGE_NAME = 'asagao-for-minecraft-'+json['VM_AND_IMAGE_NAME'] if json['VM_AND_IMAGE_NAME'] != '' else 'asagao-for-minecraft'
    ADMIN_USER_ID = json['ADMIN_USER_ID'] 
    DISCORD_CHANNEL_NAMES = ('minecraft, minecraft-test' if json['DISCORD_CHANNEL_NAMES'] == '' else json['DISCORD_CHANNEL_NAMES']).replace(' ', '').split(',')

    # secret
    HOUR_FOR_IMAGE_LEAVE_ALONE_LONG_TIME = json.get('HOUR_FOR_IMAGE_LEAVE_ALONE_LONG_TIME')
    ALLOW_PROCESS_KILL_COMMAND = json.get('ALLOW_PROCESS_KILL_COMMAND')



if HOUR_FOR_IMAGE_LEAVE_ALONE_LONG_TIME == None:
  HOUR_FOR_IMAGE_LEAVE_ALONE_LONG_TIME = ''

if ALLOW_PROCESS_KILL_COMMAND == 'true':
  ALLOW_PROCESS_KILL_COMMAND = True
else:
  ALLOW_PROCESS_KILL_COMMAND = False
