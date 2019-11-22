import tweepy
import time
import os
import sys
import io

from tweet_generate import get_text
from give_mentions_reply import reply_to_tweets

c_k = os.environ.get('c_k')
c_s = os.environ.get('c_s')
a_k = os.environ.get('a_k')
a_s = os.environ.get('a_s')
auth = tweepy.OAuthHandler(c_k,c_s)
auth.set_access_token(a_k,a_s)
api = tweepy.API(auth)

def post_tweet():
    try:
        text = get_text()
        api.update_status(text)
    except:
        print('tweet failed')

def give_mentions_a_reply():
    try:
        reply_to_tweets(api)
    except:
        print('reply to mention process failed')

while True:
    post_tweet()
    give_mentions_a_reply()
    time.sleep(40)