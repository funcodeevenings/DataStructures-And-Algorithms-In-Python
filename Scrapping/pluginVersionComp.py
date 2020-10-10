import requests
from bs4 import BeautifulSoup

page=requests.get("https://ffc-jenkins-stage.stage.oobesaas.adobe.com:8443/pluginManager/installed",
                headers={'Authorization': 'Basic YWRpbWlzaHI6OTQxNDUyMTQ4Mi1Bbm9vcA=='})
print(page.status_code)
soup = BeautifulSoup(page.content, 'html.parser')
f=open("pluginUpdatesStage.csv","w")
plugins = list(soup.find_all(id="plugins"))[0].find_all('tr')
pluginList = []
for i,plugin in enumerate(plugins):
    #print(plugin)
    if not plugin.find(class_="pane details"):
        continue

    name = list(plugin.find(class_="pane details").find_all('div'))[0].find('a').get_text()
    current_version = plugin.find(class_='center pane').find('a').get_text()
    isUpdated = list(plugin.find_all('td'))[3].find('form')
    if isUpdated:
        previous_version=isUpdated.find('input')['value'][13:]
        line = (name,previous_version,current_version)
        
    else:
        line = (name," ",current_version)

    pluginList.append(line)

pluginList.sort()

for x in pluginList:
    name,pv,cv=x
    line=name+","+pv+","+cv
    f.write(line)
    f.write("\n")




