import time
import json
import requests
from requests_oauthlib import OAuth1


# sudo apt install python3-pip
# sudo pip3 install tweepy
import tweepy

from credentials import *


# todo: python month text to number

url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)
requests.get(url, auth=auth)


userList = [
    # 'BTCTN',
    # 'rogerkver',
    'VitalikButerin',
    # 'justinsuntron',
    # 'Huobi_Pro',
    'jakehdchoi'
]

count = 5
exclude_replies = 'false'
include_rts = 'true'






def pjson(a):
    return json.dumps(a, indent=2, sort_keys=True)

def get_user_timeline(screen_name, count, exclude_replies, include_rts):
    try:
        r = requests.get('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=' + screen_name + '&count=' + str(count) + '&exclude_replies=' + exclude_replies + '&include_rts=' + include_rts + '&tweet_mode=extended', auth=auth)
        return r.json()
    except:
        print(str(r.status_code) + ' err: get_user_timeline')
        print(r.raise_for_status())
        return r.raise_for_status()



for screen_name in userList:
    res = get_user_timeline(screen_name, count, exclude_replies, include_rts)
    for tweet in res:
        print (tweet['full_text'])
        print('-----')


# for tweet in r.json():
#   # print (tweet['text'])
#   print('-----')
# # print(json.dumps(r.json(), indent=2, sort_keys=True))
# print(pjson(r.json()))

# for user in userList:
#     tweet = api.user_timeline(
#         screen_name = user,
#         count = numberOfTwits,
#         tweet_mode = "extended",
#         include_rts = False)
#     # pp = pprint.PrettyPrinter(indent=4)
#     # pp.pprint(str(tweet))
#     # print (json.dumps(tweet.__dict__, indent=4, sort_keys=True))
#     print (json.dumps(str(tweet), indent=4, sort_keys=True))
#     # print (json.dumps(tweet.__dict__))
#
#     print(len(tweet))



# my_file = open('verne.txt', 'r')
# file_lines = my_file.readlines()
# my_file.close()
#
# for line in file_lines:
# # Add try ... except block to catch and output errors
#     try:
#         print(line)
#         if line != '\n':
#             api.update_status(line)
#         else:
#             pass
#     except tweepy.TweepError as e:
#         print(e.reason)
#     time.sleep(1)







# def main():
#     print('icecandy...')
#     # time.sleep(10)
#     print(time.strftime('start: ' + '%Y-%m-%d %H:%M:%S', time.localtime()))
#
# if __name__ == "__main__":
#     main()
