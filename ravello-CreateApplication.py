import requests
import re

v_vms = input("How many machines to create?")
type(v_vms)

appId=str(3125674087857) #Application Id that should be built - corresponds to Ravello Image Id
v_search = 'id=[^>]+'
appFile = open("appFile.txt","w+")
vm=int(v_vms)

for i in range(vm):
    url = "https://cloud.ravellosystems.com/api/v1/applications/"
    
    x=str(i)
    
    payload = "{\n    \"name\" : \"HOL-"+x+"-NYC\",\n    \"baseBlueprintId\" : "+appId+"\n}"
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        }

    response = requests.request("POST", url, data=payload, headers=headers, auth=('<Ravello_Login_Id>','<pwd>'))
    
    result = re.search(v_search, response.text)
    result2=str(result)+"\n"

    appFile.write(result2)
    print(result)

appFile.close()