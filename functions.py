import json
import requests
from requests_oauthlib import OAuth1

from config import *
from credentials import *


url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)
requests.get(url, auth=auth)


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

def DictListUpdate(lis1, lis2):
    for aLis1 in lis1:
        if aLis1 not in lis2:
            lis2.append(aLis1)
    return lis2
