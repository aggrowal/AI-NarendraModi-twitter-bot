# AI-NarendraModi
Code to generate tweets for Current Indian PM Narendra Modi and post them to twitter.    
Tweets of PM narendra modi were extracted and used to train the model.    
![Snapshot of Bot Twitter account](https://github.com/rohan-aggarwal/AI-NarendraModi/blob/master/Screen%20shots/02-posted-tweets.PNG)    
Using this code a bot can be made that posts generated tweets after a certain interval (check tweet_generate.py )    
This bot can also with reply to some mentions ( check give_mentions_reply.py )        
This bot was tested by hosting it on heroku , instructions to host on heroku can be found by ![Deploy to heroku](https://devcenter.heroku.com/articles/git)    
![Logs generated after deploying bot to heroku](https://github.com/rohan-aggarwal/AI-NarendraModi/blob/master/Screen%20shots/01-heroku-logs.PNG)

# Used Libraries :
Following libraries were used in this project:    
* ![TextGenRnn](https://github.com/minimaxir/textgenrnn)
* ![Tweepy](https://github.com/tweepy/tweepy)  

# Deploying Instructions:
* Save your twitter api keys as environment variables ( can be configured in file bot.py )   
* Information on how to get twitter api keys - <a href="https://themepacific.com/how-to-generate-api-key-consumer-token-access-key-for-twitter-oauth/994/">Get Twitter Keys</a>        
* Follow instructions written in last_seen_id.txt
* If you want to use heroku use the above mentioned link
* To use locally use command python bot.py
