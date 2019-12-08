'''
This script contains code that generates tweets
'''

def generate_tweet(modi):
    '''
    This function is helper for get_text function
    It generates new tweet an saves it to a file
    '''
    modi.generate_to_file('generated_tweet.txt')

def get_text(modi):
    '''
    This function returns generated text in string format
    It requires textgenrnn's model reference
    '''
    text = ''
    while True:
        generate_tweet(modi)
        file_name = open('generated_tweet.txt', 'r')
        text = file_name.read()
        file_name.close()
        if len(text) > 139:
            continue
        else:
            break
    text = text.strip("\n\r")
    text = text.replace('\t', '').replace('\n', '').replace('   ', '')
    return text
