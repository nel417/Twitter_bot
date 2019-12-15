import tweepy as tp
import time
import os

consumer_key = 'YOUR KEY'
consumer_secret = 'YOUR SECRET'
access_token = 'YOUR TOKEN'
access_token_secret = 'YOUR SECRET TOKEN'



auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tp.API(auth)

os.chdir('pictures')
for pics in os.listdir('.'):
    api.update_with_media(pics, "#MOOD")
    time.sleep(2)
