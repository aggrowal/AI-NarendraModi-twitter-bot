import tweepy
import time
import os
import sys
import io
import urllib.parse
import urllib.request
from datetime import datetime
from tweet_generate import get_text
from give_mentions_reply import reply_to_tweets
from speech_generate import get_speech

from textgenrnn import textgenrnn
modi_tweets = textgenrnn(weights_path='tweets-model/textgenrnn_weights.hdf5',
                vocab_path='tweets-model/textgenrnn_vocab.json',
                config_path='tweets-model/textgenrnn_config.json')
modi_speech = textgenrnn(weights_path='speech-model/NarendraModi_Speech.hdf5',
                vocab_path='speech-model/textgenrnn_vocab.json',
                config_path='speech-model/textgenrnn_config.json')

c_k = os.environ.get('c_k')
c_s = os.environ.get('c_s')
a_k = os.environ.get('a_k')
a_s = os.environ.get('a_s')
pastebin_key = os.environ.get('pastebin_key')

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

def post_speech():
    try:
        text = get_speech(modi_speech)[0]
        now = datetime.now()
        url = "http://pastebin.com/api/api_post.php"
        values = {
            'api_option' : 'paste',
            'api_dev_key' : pastebin_key,
            'api_paste_code' : text,
            'api_paste_private' : '0',
            'api_paste_name' : 'AI NarendraModi Speech',
            'api_paste_expire_date' : 'N',
            'api_paste_format' : 'text',
            'api_user_key' : 'User Key Here',
            'api_paste_name' : 'speech at '+str(now)+'.txt',
        }
        data = urllib.parse.urlencode(values)
        data = data.encode('utf-8')
        req = urllib.request.Request(url, data)
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
        status = 'Read my AI generated speech here '+str(the_page)
        api.update_status(status)
        print('Completed posting speech at ',now)
    except:
        print('speech posting failed')

def give_mentions_a_reply():
    try:
        reply_to_tweets(api)
        now = datetime.now()
        print('Completed replying to mentions at ',now)
    except:
        print('reply to mention process failed')

while True:
    post_speech()
    for j in range(4):
        post_tweet()
        for i in range(0,45):
            give_mentions_a_reply()
            time.sleep(40)    