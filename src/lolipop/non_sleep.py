import os
import time
import requests

# option
LOLIPOP_MC_PROJECT_DMAIN = os.environ.get('LOLIPOP_MC_PROJECT_DMAIN', '')

if LOLIPOP_MC_PROJECT_DMAIN != '':
  while True:
    requests.get(LOLIPOP_MC_PROJECT_DMAIN)
    time.sleep(5*60)
