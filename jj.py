import urllib
import urllib2

url = 'http://imfpush.ng.bluemix.net/imfpush/v1/apps/b5af80bd-8f14-4e51-afde-7dd1b36ad2f0/messages'
appSecret = 'e1152f70-123f-4b27-bbd9-335fc2a6fb7f'
ctype = 'application/json'
values = {"message": { "alert": "Test Message" }}
headers = { 'Content-Type' : ctype,'appSecret' : appSecret }

data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
the_page = response.read()