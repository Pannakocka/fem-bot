import tweepy
from time import sleep
import json
from random import randint
from pprint import pprint
from credentials import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

with open('nouns.json') as data_file:
    list_data = json.load(data_file)

# pprint(data)
pprint(list_data[0]['masculinitive1'])
pprint(list_data[0]['feminitive1'])


def tweet():
    #for index, nouns in enumerate(list_data, index):
    while(True):
        index = index.seed()
        index = index.randint(0, 234)
        nouns = list_data[index]['feminitive1'] + " – фемінітив до слова " + list_data[index]['masculinitive1']
        try:
            print(nouns.capitalize())
            if nouns != '\n':
                api.update_status(nouns.capitalize())
                sleep(900)
            else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(10)

tweet()
