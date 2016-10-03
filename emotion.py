from nltk import wordpunct_tokenize
import json
from nltk.sentiment.util import demo_liu_hu_lexicon
import matplotlib.pyplot

fname = 'tweets.json'
with open(fname, 'r') as f:
    for line in f:
        # tweet_list - list of jsons
        tweet_list = json.loads(line)

        # append 'text' from tweet to user_tweet_list
        # tweet - single json, dictionary
        user_tweet_list = [tweet['text'] for tweet in tweet_list
        if tweet['user']['screen_name'] == "2lr"]

        for user_tweet in user_tweet_list:
            print(user_tweet)

            # print sensitivity score for twe and show plot (True)
            demo_liu_hu_lexicon(user_tweet, True)




