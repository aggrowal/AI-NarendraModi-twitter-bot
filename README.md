# Text-Generating Twitter bot    
![Snapshot of twitter account used to demonstrate the bot](https://github.com/rohan-aggarwal/text-generating-twitter-bot/blob/master/AI_Narendra_Modi.PNG)
Code to generate tweets and post them to twitter    
Tweets of PM narendra modi were extracted and used to train the model    
Using this code a bot can be made that posts generated tweets after a certain interval (check tweet_generate.py )    
This bot can also with reply to some mentions ( check give_mentions_reply.py )        
This bot was tested by hosting it on heroku , instructions to host on heroku can be found by <a href="https://devcenter.heroku.com/articles/git" target="_blank">Clicking Here</a>    

# Used Libraries :
Following libraries were used in this project:    
* <a href="https://github.com/minimaxir/textgenrnn" target="_blank">TextGenRnn</a>
* <a href="https://github.com/tweepy/tweepy" target="_blank">Tweepy</a>    

# Setup:
* Save your twitter api keys as environment variables ( can be configured in file bot.py )    
* If you want to use heroku use the above mentioned link
* To use locally use command python bot.py
