'''
This script contains code that helps to return appropriate response when the 
bot account has been mentioned.
'''

FILE_NAME = 'last_seen_id.txt'
def retrieve_last_seen_id(file_name):
    '''
    This function is a helper function and returns last id of processed tweet in
    which the bot account was mentioned
    '''
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id,file_name):
    '''
    This function is a helper function and stores id of last processed tweet
    in which the bot account was mentioned
    '''
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()

def reply_to_tweets(api):
    '''
    This function uses api to post an appropriate response to bot account
    '''
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')
    for mention in reversed(mentions):
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        test_string =  mention.full_text.lower()
        if ('#acchedin' in test_string or '#aachedin' in test_string):
            api.update_status('@' + mention.user.screen_name +
                    ' Ache din aane wale hain', mention.id)
        if '#jio' in test_string:
            api.update_status('@' + mention.user.screen_name +
                    ' Modi hai tho mumkin hai', mention.id)
        if '#climate' in test_string:
            api.update_status('@' + mention.user.screen_name +
                    ' Yeh climate change nahin hua hai, hum change ho gaye hain', mention.id)
        if '#rahulgandhi' in test_string:
            api.update_status('@' + mention.user.screen_name +
                    ' sahabjaadein', mention.id)
