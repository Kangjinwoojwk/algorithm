import requests
import urllib.request
import json

url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=901"
request = requests.get(url)
data = request.content
da = json.loads(data)
print(request)
print(data)
print(da)

request = urllib.request.Request(url)
response_body = urllib.request.urlopen(request).read()
response = json.loads(response_body)
print(request)
print(response_body)
print(response)
