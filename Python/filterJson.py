import requests
import json
import yaml

url = "https://prod-rel-ffc.oobesaas.adobe.com/adobe-ffc-external/core/v1/3271EE9E-C93C-4C39-8E65-949957707C9B/builds"
resp = requests.get(url,headers={'Accept':'application/json'})
cont = resp.content
js = yaml.safe_load(cont)
builds = js["build"]
i=0
for x in builds:
    if x["version"].startswith("0"):
        i=i+1
        print(i,x["productId"],x["version"],x["platform"])
