import urllib, urllib2 
import base64
import json

c_key = ''
c_secret = ''

screen_name = "Therp_BV"
count = '25'
base_api_path = "https://api.twitter.com/1.1/"
proxies = {'https': 'https://www.therp.nl'}

def get_token(c_key, c_secret):
    args = {
            'grant_type': 'client_credentials'
            }
    url = 'https://api.twitter.com/oauth2/token'
    credentials = base64.b64encode(c_key + ':' + c_secret)
    data = urllib.urlencode(args)
    request = urllib2.Request(url, data=data)
    request.add_header("Authorization", "Basic %s" % credentials)
    request.add_header(
        'content-type',  'application/x-www-form-urlencoded;charset=UTF-8'
    )
    response = urllib2.urlopen(request)
    response_str = response.read()
    print response_str 
    response_dict = json.loads(response_str)
    return str(response_dict['access_token'])



def get_feed(token):
    args = {
            'screen_name': screen_name,
            'count':'2',
            } 
    url = base_api_path + "statuses/home_timeline.json"
    data = urllib.urlencode(args)
    request = urllib2.Request(url)
    request.add_header(
      "Authorization",  "Bearer %s" %  token
    )
    request.add_header(
        'content-type',  'application/x-www-form-urlencoded;charset=UTF-8'
    )
    response = urllib2.urlopen(request)
    return response.read()    


token = get_token(c_key, c_secret)
tweets = get_feed(token)
print tweets
