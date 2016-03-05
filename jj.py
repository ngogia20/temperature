import requests
import json 


url = 'http://imfpush.ng.bluemix.net/imfpush/v1/apps/b5af80bd-8f14-4e51-afde-7dd1b36ad2f0/messages'
appSecret = 'e1152f70-123f-4b27-bbd9-335fc2a6fb7f'
ctype = 'application/json'
values = {"message": { "alert": "Test Message from pi" }}
head = { 'Content-Type' : ctype,'appSecret' : appSecret }


req = requests.post(url, data=json.dumps(values), headers=head)


