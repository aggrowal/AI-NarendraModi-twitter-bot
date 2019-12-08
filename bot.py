'''
This script contains code to handle the bot account's functions
'''

import time
import os
import urllib.parse
import urllib.request
from datetime import datetime
import tweepy
from textgenrnn import textgenrnn
from tweet_generate import get_text
from give_mentions_reply import reply_to_tweets
from speech_generate import get_speech

MODI_TWEETS = textgenrnn(weights_path='tweets-model/textgenrnn_weights.hdf5',
                vocab_path='tweets-model/textgenrnn_vocab.json',
                config_path='tweets-model/textgenrnn_config.json')
MODI_SPEECH = textgenrnn(weights_path='speech-model/NarendraModi_Speech.hdf5',
                vocab_path='speech-model/textgenrnn_vocab.json',
                config_path='speech-model/textgenrnn_config.json')

CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_KEY = os.environ.get('ACCESS_KEY')
ACCESS_SECRET = os.environ.get('ACCESS_SECRET')
PASTEBIN_KEY = os.environ.get('PASTEBIN_KEY')

AUTH = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
AUTH.set_access_token(ACCESS_KEY,ACCESS_SECRET)
API = tweepy.API(AUTH)

def post_tweet():
    '''
    Helper fucnction to facilitate tweet posting functionality
    '''
    try:
        text = get_text(MODI_TWEETS)
        API.update_status(text)
        now = datetime.now()
        print('Completed posting tweet at ', now)
    except:
        print('tweet failed')

def post_speech():
    '''
    Helper function to facilitate speech posting functionality
    '''
    try:
        text = get_speech(MODI_SPEECH)[0]
        now = datetime.now()
        url = "http://pastebin.com/api/api_post.php"
        values = {
            'api_option' : 'paste',
            'api_dev_key' : PASTEBIN_KEY,
            'api_paste_code' : text,
            'api_paste_private' : '0',
            'api_paste_name' : 'AI NarendraModi Speech',
            'api_paste_expire_date' : 'N',
            'api_paste_format' : 'text',
            'api_user_key' : 'User Key Here',
        }
        data = urllib.parse.urlencode(values)
        data = data.encode('utf-8')
        req = urllib.request.Request(url, data)
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
        status = 'Read my AI generated speech here '+ str(the_page)
        API.update_status(status)
        print('Completed posting speech at ', now)
    except:
        print('speech posting failed')

def give_mentions_a_reply():
    '''
    Helper function to facilitate reply funtionality
    '''
    try:
        reply_to_tweets(API)
        now = datetime.now()
        print('Completed replying to mentions at ', now)
    except:
        print('reply to mention process failed')

while True:
    post_speech()
    for j in range(4):
        post_tweet()
        for i in range(0, 45):
            give_mentions_a_reply()
            time.sleep(40)    