import os
import sys
import requests
import json

URL = "https://whatsinmess.vercel.app/api/get_menu"

response = requests.get(URL)
response_json = response.json()

# 
with open('data.json', 'w') as f:
    json.dump(response_json, f, indent=4)
#