# Python script to analyze 
# emotion of image 
import http.client, urllib.request 
import urllib.parse, urllib.error 
import base64, sys 
import simplejson as json 
  
# replace with subscription_key 
# you obtained after registration 
subscription_key = '12f29133caf4406493e81b6a31c47c1a'
  
headers = { 
  
    # Request headers. Replace 
    # the placeholder key 
    # below with your 
    # subscription key. 
    'Content-Type': 'application/json', 
    'Ocp-Apim-Subscription-Key': subscription_key, 
} 
  
params = urllib.parse.urlencode({ 
}) 
  
# Replace the URL 
# below with the 
# URL of the image 
# you want to analyze. 
url1 = 'IMAGE URL TO BE ADDED HERE'
body = { 'url': url1 } 
newbody =str(body) 
  
try: 
    # NOTE: You must use the same region in your REST call as you used to obtain your subscription keys. 
    # For example, if you obtained your subscription keys from westcentralus, replace "westus" in the 
    # URL below with "westcentralus". 
    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com') 
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, newbody, headers) 
    response = conn.getresponse() 
    data = response.read() 
  
    parsed = json.loads(data) 
    print ("Response:") 
    print (json.dumps(parsed, sort_keys=True, indent=2)) 
  
    # the emotion of image 
    # will the max value of 
    # any emotion obtained 
    # from the different 
    # scores of each emotion 
    val = parsed[0]["scores"] 
    res = max(val, key = val.get) 
    print ("\nEmotion :: ",res) 
  
    conn.close() 
except Exception as e: 
    print(e.args) 
