########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'ba10a036532d4c438ded719c0f797a4e',
    'Ocp-Apim-Subscription-Key': 'ba10a036532d4c438ded719c0f797a4e',
}

params = urllib.parse.urlencode({
    # Request parameters
    'image': 'https://contestimg.wish.com/api/webimage/5c394bfbe3e6604287a573da-large.jpg?cache_buster=276746c000af54b686498893ade2baea',
    # 'gender': '{string}',
   # 'limit': '1',
})

conn = http.client.HTTPSConnection('api.mirrorthatlook.com')
conn.request("GET", "/v2/mirrorthatlook?%s" % params, "{body}", headers)
response = conn.getresponse()
data = response.read()
    # print(data)

my_json = data.decode('utf8')
python_obj = json.loads(my_json)

loaded_json = json.dumps(my_json)
loaded_json = json.loads(my_json)

#this works to classify the group that the item is in from the image
print((loaded_json["result"][0]["group"]))


print(loaded_json)
print((loaded_json["result"][0]["products"][0]["affiliates"][0]["link"]))
for x in range(22):
    print((loaded_json["result"][0]["products"][x]["affiliates"][0]["link"]))
#new_json = str(new_json).strip('[]')





#print(python_obj.items())
#for i in python_obj:
 #   print(i, python_obj[i])
#for key,value in python_obj.items():
#    print(key + " => " + value)

conn.close()