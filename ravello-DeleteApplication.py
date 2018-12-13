import requests

ids = ('<application id>', 'test') #Application Id is the ID that is created when the application was created

for id in ids:
    url = "https://cloud.ravellosystems.com/api/v1/applications/"+id
    
    payload = ""
    
    headers = {
    'cache-control': "no-cache",
    }
    
    response = requests.request("DELETE", url, data=payload, headers=headers, auth=('<Ravello_Login_Id>','<pwd>'))
    
    print(response.text)