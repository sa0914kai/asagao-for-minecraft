import sys
import time
import discord
import requests
import json
import utility
from config import *
import logger_wrap

logger = logger_wrap.logger(__name__)


async def get_conoha_api_token(_message):
  logger.info('get_conoha_api_token')
  headers = {'Accept': 'application/json'}
  data = {
    'auth': {
      'passwordCredentials': {
        'username': CONOHA_API_USER_NAME, 
        'password': CONOHA_API_USER_PASSWORD
      },
      'tenantId': CONOHA_API_TENANT_ID
    }
  }
  try:
    response = requests.post(CONOHA_API_IDENTITY_SERVICE+'/tokens', data=json.dumps(data), headers=headers)
    if response.status_code == 200:
      return (json.loads(response.text))['access']['token']['id']
    else:
      await utility.post_embed_failed(_message, 'post CONOHA_API_IDENTITY_SERVICE/tokens: #{response.status_code}.')
      return None
  except requests.exceptions.RequestException as e:
    utility.post_embed_failed(_message, 'post CONOHA_API_IDENTITY_SERVICE/tokens: RequestException.')
    return None


async def get_images(_message):
  logger.info('get_images')
  conoha_api_token = await get_conoha_api_token(_message)
  if conoha_api_token == None:
    return None
  headers = {'Accept': 'application/json', 'X-Auth-Token': conoha_api_token}
  try:
    response = requests.get(CONOHA_API_IMAGE_SERVICE+'/v2/images', headers=headers)
    logger.info(f'response.status_code: {response.status_code}\n\
      response.text: \n\
      {json.loads(response.text)}\n')
    if response.status_code == 200:
      images = json.loads(response.text)['images']
      images = [i for i in images if i['name'] == VM_AND_IMAGE_NAME]
      if len(images) >= 2:
        await utility.post_embed_error(_message, f'Exist multi images(name :{VM_AND_IMAGE_NAME}).')
        sys.exit()
      return images
    else:
      await utility.post_embed_failed(_message, 'get CONOHA_API_IMAGE_SERVICE/v2/images: #{response.status_code}.')
      return None
  except requests.exceptions.RequestException as e:
    await utility.post_embed_failed(_message, 'get CONOHA_API_IMAGE_SERVICE/v2/images: RequestException.')
    return None


async def get_image_status(_message, _image):
  logger.info('get_image_status')
  if _image == None:
    await utility.post_embed_failed(_message, 'Could not get image id.')
    return None
  image_id = _image['id']

  conoha_api_token = await get_conoha_api_token(_message)
  if conoha_api_token == None:
    return None
  headers = {'Accept': 'application/json', 'X-Auth-Token': conoha_api_token}
  try:
    response = requests.get(CONOHA_API_COMPUTE_SERVICE+'/images/'+image_id, headers=headers)
    logger.info(f'response.status_code: {response.status_code}\n\
      response.text: \n\
      {json.loads(response.text)}\n')
    if response.status_code == 200:
      image_status = json.loads(response.text)['image']['status']
      return image_status
    else:
      await utility.post_embed_failed(_message, 'get CONOHA_API_COMPUTE_SERVICE/images/[image_id]: #{response.status_code}.')
      return None
  except requests.exceptions.RequestException as e:
    await utility.post_embed_failed(_message, 'CONOHA_API_COMPUTE_SERVICE/images/[image_id]: RequestException.')
    return None


async def get_servers_for_minecraft(_message):
  logger.info('get_servers_for_minecraft')
  conoha_api_token = await get_conoha_api_token(_message)
  if conoha_api_token == None:
    return None
  headers = {'Accept': 'application/json', 'X-Auth-Token': conoha_api_token}
  try:
    response = requests.get(CONOHA_API_COMPUTE_SERVICE+'/servers/detail', headers=headers)
    logger.info(f'response.status_code: {response.status_code}\n\
      response.text: \n\
      {json.loads(response.text)}\n')
    if response.status_code == 200:
      servers = json.loads(response.text)['servers']
      servers = [s for s in servers if s['metadata']['instance_name_tag'] == VM_AND_IMAGE_NAME]
      if len(servers) >= 2:
        await utility.post_embed_error(_message, f'Exist multi VMs(name :{VM_AND_IMAGE_NAME}).')
        sys.exit()
      return servers
      # status: ['ACTIVE', 'SHUTOFF', 'BUILD']
    else:
      await utility.post_embed_failed(_message, 'get CONOHA_API_COMPUTE_SERVICE/servers/detail: #{response.status_code}.')
      return None
  except requests.exceptions.RequestException as e:
    await utility.post_embed_failed(_message, 'get CONOHA_API_COMPUTE_SERVICE/servers/detail: RequestException.')
    return None


async def exist_both_vm_and_image(_message):
  logger.info('exist_both_vm_and_image')
  images = await get_images(_message)
  if images == None:
    await utility.post_embed_failed(_message, ' Could not get images.')
    return None
  image_status = await get_image_status(_message, images[0])
  servers = await get_servers_for_minecraft(_message)
  if image_status == None or servers == None:
    await utility.post_embed_failed(_message, 'Could not get image_status or servers.')
    return None
  if len(servers) == 0:
    await utility.post_embed_failed(_message, 'Not Exist servers.')
    return False
  server_status = servers[0]['status']
  if image_status == 'ACTIVE' and (server_status in ['ACTIVE', 'SHUTOFF']):
    return True
  return False
