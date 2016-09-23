from nltk import wordpunct_tokenize
import json
from collections import Counter
 
fname = 'tweets.json'
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
s
        all_users = [term  for tw in tweet for term in wordpunct_tokenize(tw['user']['screen_name'])]

        count_all.update(all_users)
    print(count_all.most_common(30))