import tweepy
import time
import os
import sys
import io

from tweet_generate import return_tweet

c_k = os.environ.get('c_k')
c_s = os.environ.get('c_s')
a_k = os.environ.get('a_k')
a_s = os.environ.get('a_s')
auth = tweepy.OAuthHandler(c_k,c_s)
auth.set_access_token(a_k,a_s)
api = tweepy.API(auth)

auth = tweepy.OAuthHandler(c_k,c_s)
auth.set_access_token(a_k,a_s)
api = tweepy.API(auth)
FILE_NAME = 'last_seen_id.txt'
def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id
def store_last_seen_id(last_seen_id,file_name):
    f_write = open(file_name,'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')
    for mention in reversed(mentions):
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        test_string =  mention.full_text.lower()
        if ('#acchedin' in test_string or '#aachedin' in test_string):
            api.update_status('@' + mention.user.screen_name +
                    ' Ache din aane wale hain', mention.id)
        elif '#jio' in test_string:
            api.update_status('@' + mention.user.screen_name +
                    ' Modi hai tho mumkin hai', mention.id)
        elif '#climate' in test_string:
            api.update_status('@' + mention.user.screen_name +
                    ' Yeh climate change nahin hua hai, hum change ho gaye hain', mention.id)
        elif '#rahulgandhi' in test_string:
            api.update_status('@' + mention.user.screen_name +
                    ' sahabjaadein', mention.id)
        elif '#rtvideo' in test_string or '#rtarticle' in test_string or '#rtpic' in test_string:
            api.retweet(mention.id)
    print('done with replies')
def post_tweet():
    api.update_status(return_tweet())
    print('Done with tweet')

while True:
    print('start')
    post_tweet()
    print('main fn tweet')
    reply_to_tweets()
    print('main fn reply')
    print('sleeping')
    time.sleep(20)
    print('sleep over')