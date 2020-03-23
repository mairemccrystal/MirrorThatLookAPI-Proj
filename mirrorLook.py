########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'ba10a036532d4c438ded719c0f797a4e',
    'Ocp-Apim-Subscription-Key': 'ba10a036532d4c438ded719c0f797a4e',
}

params = urllib.parse.urlencode({
    # Request parameters
    'image': 'https://contestimg.wish.com/api/webimage/5c394bfbe3e6604287a573da-large.jpg?cache_buster=276746c000af54b686498893ade2baea',
    #'gender': '{string}',
    #'limit': '{string}',
})

try:
    conn = http.client.HTTPSConnection('api.mirrorthatlook.com')
    conn.request("GET", "/v2/mirrorthatlook?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
   # print(data)

    my_json = data.decode('utf8')
    print (my_json)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))



####################################