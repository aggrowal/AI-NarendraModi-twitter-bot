import tweepy
import time
import os
import sys
import io
from datetime import datetime
from tweet_generate import get_text
from give_mentions_reply import reply_to_tweets

from textgenrnn import textgenrnn
modi_tweets = textgenrnn(weights_path='tweets-model/textgenrnn_weights.hdf5',
                vocab_path='tweets-model/textgenrnn_vocab.json',
                config_path='tweets-model/textgenrnn_config.json')

c_k = os.environ.get('c_k')
c_s = os.environ.get('c_s')
a_k = os.environ.get('a_k')
a_s = os.environ.get('a_s')

auth = tweepy.OAuthHandler(c_k,c_s)
auth.set_access_token(a_k,a_s)
api = tweepy.API(auth)

def post_tweet():
    try:
        text = get_text(modi_tweets)
        api.update_status(text)
        now = datetime.now()
        print('Completed posting tweet at ',now)
    except:
        print('tweet failed')

def give_mentions_a_reply():
    try:
        reply_to_tweets(api)
        now = datetime.now()
        print('Completed replying to mentions at ',now)
    except:
        print('reply to mention process failed')

while True:
    post_tweet()
    for i in range(0,45):
        give_mentions_a_reply()
        time.sleep(40)