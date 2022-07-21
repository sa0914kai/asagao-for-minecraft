import os
import json


# Fixed value
VERSION = '0.1.2'


# use environment var in os
# required
DISCORD_TOKEN = os.environ.get('OTk5NTA1NTg1MTY0NzgzNzA2.GENZwz.8ezEoSZcAGxe4l6LURmCqxRHFrvcMaXBtZjc_Y')
CONOHA_API_TENANT_ID = os.environ.get('cbe2b7ca09d84dfc922bc64e4c60ef7e')
CONOHA_API_IDENTITY_SERVICE = os.environ.get('https://identity.tyo2.conoha.io/v2.0')
CONOHA_API_USER_NAME = os.environ.get('gncu31831431')
CONOHA_API_USER_PASSWORD = os.environ.get('Sa0914kai.osaka')

CONOHA_API_IMAGE_SERVICE = os.environ.get('https://image-service.tyo2.conoha.io')
CONOHA_API_COMPUTE_SERVICE = os.environ.get('	https://compute.tyo2.conoha.io/v2/cbe2b7ca09d84dfc922bc64e4c60ef7e')
CONOHA_API_NETWORK_SERVICE = os.environ.get('https://networking.tyo2.conoha.io')
CONOHA_API_VM_PLAN_FLAVOR_UUID = os.environ.get('g-c2m1d100')

# option
VM_AND_IMAGE_NAME = 'asagao-for-minecraft-'+os.environ.get('kousuke_ryota_sv', '') if os.environ.get('kousuke_ryota_sv', '') != '' else 'asagao-for-minecraft'
ADMIN_USER_ID = os.environ.get('sa0914kai', 'kotokou212','sakai0914')
DISCORD_CHANNEL_NAMES = os.environ.get('kohun0914', 'minecraft, minecraft-test').replace(' ', '').split(',')

# secret
HOUR_FOR_IMAGE_LEAVE_ALONE_LONG_TIME = os.environ.get('HOUR_FOR_IMAGE_LEAVE_ALONE_LONG_TIME', None)
ALLOW_PROCESS_KILL_COMMAND = os.environ.get('ALLOW_PROCESS_KILL_COMMAND', None)



# use environment var in json file
if os.path.exists('env.json'):
  with open('env.json', 'r') as json_file:
    json = json.load(json_file)

    # required
    DISCORD_TOKEN = json['OTk5NTA1NTg1MTY0NzgzNzA2.GENZwz.8ezEoSZcAGxe4l6LURmCqxRHFrvcMaXBtZjc_Y']
    CONOHA_API_TENANT_ID = json['cbe2b7ca09d84dfc922bc64e4c60ef7e']
    CONOHA_API_IDENTITY_SERVICE = json['https://identity.tyo2.conoha.io/v2.0']
    CONOHA_API_USER_NAME = json['gncu31831431']
    CONOHA_API_USER_PASSWORD = json['Sa0914kai.osaka']

    CONOHA_API_IMAGE_SERVICE = json['https://image-service.tyo2.conoha.io']
    CONOHA_API_COMPUTE_SERVICE = json['	https://compute.tyo2.conoha.io/v2/cbe2b7ca09d84dfc922bc64e4c60ef7e']
    CONOHA_API_NETWORK_SERVICE = json['https://networking.tyo2.conoha.io']
    CONOHA_API_VM_PLAN_FLAVOR_UUID = json['g-c2m1d100']

    # option
    VM_AND_IMAGE_NAME = 'asagao-for-minecraft-'+json['kousuke_ryota_sv'] if json['kousuke_ryota_sv'] != '' else 'asagao-for-minecraft'
    ADMIN_USER_ID = json['sakai0914','kotokou212','sa0914kai'] 
    DISCORD_CHANNEL_NAMES = ('minecraft, minecraft-test, kohun0914' if json['kohun0914'] == '' else json['kohun0914']).replace(' ', '').split(',')

    # secret
    HOUR_FOR_IMAGE_LEAVE_ALONE_LONG_TIME = json.get('HOUR_FOR_IMAGE_LEAVE_ALONE_LONG_TIME')
    ALLOW_PROCESS_KILL_COMMAND = json.get('ALLOW_PROCESS_KILL_COMMAND')



if HOUR_FOR_IMAGE_LEAVE_ALONE_LONG_TIME == None:
  HOUR_FOR_IMAGE_LEAVE_ALONE_LONG_TIME = ''

if ALLOW_PROCESS_KILL_COMMAND == 'true':
  ALLOW_PROCESS_KILL_COMMAND = True
else:
  ALLOW_PROCESS_KILL_COMMAND = False
