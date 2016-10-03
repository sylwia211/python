from nltk import wordpunct_tokenize
import json
from collections import Counter
 
fname = 'tweets.json'
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
    	#tweets - list of all tweets
        tweet_list = json.loads(line)

        #append username to all_users list
        all_users = [username for tweet in tweet_list for username in wordpunct_tokenize(tweet['user']['screen_name'])]

        #update counter
        count_all.update(all_users)
    print(count_all.most_common(30))