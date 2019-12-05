# AI-NarendraModi-twitter-Bot
Link to bot account - <a href="https://twitter.com/AINarendraModi">AI Narendra Modi</a>    
* Generates tweets and speech for Current Indian PM Narendra Modi using RNNs and post them to twitter.    
* Tweets of PM narendra modi were extracted and used to train the model.    
![Snapshot of Bot Twitter account](https://github.com/rohan-aggarwal/AI-NarendraModi/blob/master/Screen%20shots/03-account.PNG)    
* Using this code a bot can be made that posts generated tweets after a certain interval    
* This bot generates speech that is uploaded to pastebin and link is posted to twitter
* This bot can also with reply to some mentions ( check give_mentions_reply.py )        
* This bot was tested by hosting it on heroku , instructions to host on heroku can be found by <a href="https://devcenter.heroku.com/articles/git">Deploy to heroku</a>        
![Logs generated after deploying bot to heroku](https://github.com/rohan-aggarwal/AI-NarendraModi/blob/master/Screen%20shots/01-heroku-logs.PNG)

# Used Libraries :
Following libraries were used in this project:    
* <a href="https://github.com/minimaxir/textgenrnn">TextGenRnn</a>
* <a href="https://github.com/tweepy/tweepy">Tweepy</a>  

# Deploying Instructions:
* Save your twitter api keys as environment variables ( can be configured in file bot.py )   
* Information on how to get twitter api keys - <a href="https://themepacific.com/how-to-generate-api-key-consumer-token-access-key-for-twitter-oauth/994/">Get Twitter Keys</a>  
* Pastebin developer key is also needed so that speeches can be uploaded and posted by the bot    
* Follow instructions written in last_seen_id.txt
* If you want to use heroku use the above mentioned link
* To use locally use command python bot.py
