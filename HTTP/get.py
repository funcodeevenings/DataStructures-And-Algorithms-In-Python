import requests

url="https://qe-prstg-ffc.oobesaas.adobe.com/adobe-ffc-external/core/v1/3271EE9E-C93C-4C39-8E65-949957707C9B/overrides"
params={
    "channel":"*",
    "sapCode":"SPRK",
    "version":"8.0.10",
    "platform":"osx10-64"}

r = requests.get(url=url,params=params)
data = r.json()
print(data)

data = data['override']
for js in data:
    print(js['id'])