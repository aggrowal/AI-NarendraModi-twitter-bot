'''
This script contains code to generate speech text
'''

def generate_speech(modi):
    '''
    Helper function for get_speech
    Generates speech for the provided model reference and returns the text in string format
    '''
    temp = modi.generate(max_gen_length=6000, top_n=5, return_as_list=True)[0]
    temp = temp.split('\n\n')
    temp.append('\nमुझे यहां बात करने का आपने अवसर दिया, इसके लिए भी मैं आपका बहुत आभारी हूं।बहुत-बहुत धन्‍यवाद।')
    return temp

def get_speech(modi):
    '''
    Returns finalized version of text in string format
    '''
    text = generate_speech(modi)
    return text
