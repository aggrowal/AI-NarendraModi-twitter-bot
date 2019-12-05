def generate_tweet(modi):
    modi.generate_to_file('generated_tweet.txt')

def get_text(modi):
    text = ''
    while True:
        generate_tweet(modi)
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