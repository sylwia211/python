import json
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords



def calculate_languages_ratios(text):

    languages_ratios = {}

    tokens = wordpunct_tokenize(text)
    words = [word.lower() for word in tokens]

    # count number of unique stopwords per language included in nltk
    for language in stopwords.fileids():
        stopwords_set = set(stopwords.words(language))
        words_set = set(words)
        common_elements = words_set.intersection(stopwords_set)

        languages_ratios[language] = len(common_elements) # language "score"

    return languages_ratios


def detect_language(text):
    ratios = calculate_languages_ratios(text)
    most_rated_language = max(ratios, key=ratios.get)
    return most_rated_language


fname = 'tweets.json'
with open(fname, 'r') as f:
    for line in f:
        tweet_list = json.loads(line)

        # get text for 5th element
        tweet = tweet_list[5]['text']
        print(tweet)
        language = detect_language(twewt)
        print (language)