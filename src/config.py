import os
import json


# use environment var in os
# Fixed value
VERSION = '0.1.0'

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


# use environment var in json file
if os.path.exists('env.json'):
  json_file = open('env.json', 'r')
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
NOTICE_HOUR_FOR_IMAGE_LEAVE_ALONE_LONG_TIME = os.environ.get('NOTICE_HOUR_FOR_IMAGE_LEAVE_ALONE_LONG_TIME', '')
