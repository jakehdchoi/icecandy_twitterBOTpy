import time
import json
import requests
from requests_oauthlib import OAuth1

from config import *
from credentials import *


global tm_wday, tm_mon, tm_mday, tm_clock, tm_zone, tm_year, struct_time
global unionData

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

def merge_without_duplicate(lis1, lis2):
    for aLis1 in lis1:
        if aLis1 not in lis2:
            lis2.append(aLis1)
    return lis2

def convert_created_at_into_NumString(created_at):
    tm_wday, tm_mon, tm_mday, tm_clock, tm_zone, tm_year = created_at.split()
    struct_time = time.strptime(tm_mon, '%b')
    if struct_time.tm_mon < 10:
        return str(tm_year) + '0' + str(struct_time.tm_mon) + str(tm_mday)
    else:
        return str(tm_year) + str(struct_time.tm_mon) + str(tm_mday)

def convert_gmtime_into_NumString():
    thisTime = time.gmtime()
    if thisTime.tm_mon < 10:
        if thisTime.tm_mday < 10:
            return str(thisTime.tm_year) + '0' + str(thisTime.tm_mon) + '0' + str(thisTime.tm_mday)
        else:
            return str(thisTime.tm_year) + '0' + str(thisTime.tm_mon) + str(thisTime.tm_mday)
    else:
        if thisTime.tm_mday < 10:
            return str(thisTime.tm_year) + str(thisTime.tm_mon) + '0' + str(thisTime.tm_mday)
        else:
            return str(thisTime.tm_year) + str(thisTime.tm_mon) + str(thisTime.tm_mday)
