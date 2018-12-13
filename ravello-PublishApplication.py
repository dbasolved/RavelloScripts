import requests

ids = ('<application id>', 'test') #Application Id is the ID that is created when the application was created

for id in ids:
        url = "https://cloud.ravellosystems.com/api/v1/applications/"+id+"/publish"
        
        payload = "{\n\t\"preferredRegion\": \"US-East-5\",\n    \"optimizationLevel\": \"PERFORMANCE_OPTIMIZED\",\n    \"startAllVms\": \"true\"\n}"
        
        headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        }
        
        response = requests.request("POST", url, data=payload, headers=headers, auth=('<Ravello_Login_Id>','<pwd>'))
        
        print(response.text)