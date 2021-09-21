import requests
import json

client_id = "kc2pT9AIwE9nQiNbkGCr"
client_secret = "3_1niwGG_X"
url = "https://openapi.naver.com/v1/datalab/search"
body = json
print(body)
request = requests.get(url)
print(request)