import oauth2 as oauth
import urllib
import json

c_key = ''
c_secret = ''

ACCESS_KEY =  ''
ACCESS_SECRET = ''


screen_name = "Therp_BV"
count = '25'

consumer = oauth.Consumer(key=c_key, secret=c_secret)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

timeline_endpoint = "https://api.twitter.com/1.1/statuses/user_timeline.json"
params = {
        'sreen_name': screen_name,
        'count':'2',
    }
params_enc = urllib.urlencode(params)
header =  { 'Content-Type':  'application/x-www-form-urlencoded'}
response, data = client.request(timeline_endpoint)

tweets = json.loads(data)
for tweet in tweets:
        print tweet['text']
