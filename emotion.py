#import sys
from nltk import wordpunct_tokenize
import json
from nltk.sentiment.util import demo_liu_hu_lexicon
import matplotlib.pyplot


fname = 'tweets.json'
with open(fname, 'r') as f:
    for line in f:
        tweet = json.loads(line)

        all_tweets = [tw['text'] for tw in tweet
        if tw['user']['screen_name'] == "2lr"]

        for twe in all_tweets:
            print(twe)
            demo_liu_hu_lexicon(twe, True)




