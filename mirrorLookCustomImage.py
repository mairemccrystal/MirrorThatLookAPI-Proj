########## Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'ba10a036532d4c438ded719c0f797a4e',
    'Ocp-Apim-Subscription-Key': 'ba10a036532d4c438ded719c0f797a4e',
}

params = urllib.parse.urlencode({
'image' : 'file:///C:/Users/User/Desktop/python%20component/data/20.jpeg,'
}
)

conn = http.client.HTTPSConnection('api.mirrorthatlook.com')
conn.request("POST", "file:///C:/Users/User/Desktop/python%20component/data/20.jpeg" % params, "{body}", headers)
response = conn.getresponse()
data = response.read()
print(data)
conn.close()


####################################