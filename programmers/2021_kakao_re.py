import requests
import urllib.request
import json

BASE_URL = 'https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users'
request = requests.post(BASE_URL)
data = request.content
da = json.loads(data)
print(request)
print(data)
print(da)

request = urllib.request.Request(BASE_URL)
response_body = urllib.request.urlopen(request).read()
response = json.loads(response_body)
print(request)
print(response_body)
print(response)