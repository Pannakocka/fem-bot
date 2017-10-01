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
    index = randint(0, 234)
    for index, nouns in enumerate(list_data, index):
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
            sleep(85000)

tweet()


# # Read lines one by one from my_file and assign to file_lines variable
# file_lines = data_file.readlines()

# my_file=open('verne.txt','r')
# file_lines=my_file.readlines()
# my_file.close()

# for line in list_data:
#     print(line[0]['masculinitive1'])
#     api.update_status(line)

# # Create a for loop to iterate over file_lines
# for line in file_lines:
#     print(line)
#     api.update_status(line)
