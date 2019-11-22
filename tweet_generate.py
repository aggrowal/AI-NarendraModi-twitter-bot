import tweepy
import time
import os
import sys
import io
from textgenrnn import textgenrnn
modi = textgenrnn('NarendraModi.hdf5')
f = io.StringIO()

def generate_tweet():
    try:
        modi.generate(temperature=0.5)
    except:
        print('Generate_Tweet')
        sys.exit()
def validate_tweet():
    try:
        import os
        from contextlib import redirect_stdout
        out = ''
        while True:
            with redirect_stdout(f):
                generate_tweet()
            out = f.getvalue()
            if len(out) > 139:
                continue
            else:
                break
        print('validate_tweet fn')
        return out
    except:
        print('Validate_Tweet')
        return -1
def correct_tweet():
    try:
        tweet = validate_tweet()
        if tweet == -1:
            return -1
        from textblob import TextBlob
        tweet = TextBlob(tweet)
        tweet =  tweet.correct().strip("\n\r")
        print('correct_tweet fn')
        return str(tweet)
    except:
        print('Correct_Tweet')
        return -1
def final_tweet():
    try:
        text = correct_tweet()
        print('generated new tweet')
        return text.replace('\t', '').replace('\n', '').replace('   ','')
    except:
        sys.exit()
        print('Final_Tweet')
def return_tweet():
    return final_tweet()