import tweepy
import time
import os
import sys
import io
from textgenrnn import textgenrnn
modi = textgenrnn('NarendraModi.hdf5')

def generate_tweet():
    modi.generate_to_file('generated_tweet.txt')

def get_text():
    text = ''
    while True:
        generate_tweet()
        f = open('generated_tweet.txt','r')
        text = f.read()
        f.close()
        if len(text) > 139 :
            continue
        else:
            break
    text = text.strip("\n\r")
    text = text.replace('\t', '').replace('\n', '').replace('   ','')
    return text