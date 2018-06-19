import time
import json
import requests
from requests_oauthlib import OAuth1

from config import *
from credentials import *


global tm_wday, tm_mon, tm_mday, tm_clock, tm_zone, tm_year, struct_time
global unionData, sortedData

auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)
# url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
# requests.get(url, auth=auth)


def pjson(a):
    return json.dumps(a, indent=2, sort_keys=True)

def get_user_timeline(screen_name, count, exclude_replies, include_rts):
    try:
        r = requests.get('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=' + screen_name + '&count=' + str(count) + '&exclude_replies=' + exclude_replies + '&include_rts=' + include_rts + '&tweet_mode=extended', auth=auth)
        return r.json()
    except:
        print(' ' + str(r.status_code) + ' err: get_user_timeline')
        print(r.raise_for_status())
        return r.raise_for_status()

def merge_without_duplicate(lis1, lis2):
    for aLis1 in lis1:
        if aLis1 not in lis2:
            lis2.append(aLis1)
    return True

def convert_created_at_into_NumString(created_at):
    tm_wday, tm_mon, tm_mday, tm_clock, tm_zone, tm_year = created_at.split()
    struct_time = time.strptime(tm_mon, '%b')
    if struct_time.tm_mon < 10:
        return str(tm_year) + '0' + str(struct_time.tm_mon) + str(tm_mday)
    else:
        return str(tm_year) + str(struct_time.tm_mon) + str(tm_mday)

def convert_gmtime_into_NumString(gmtime):
    # print(len(res))mtime):
    if gmtime.tm_mon < 10:
        if gmtime.tm_mday < 10:
            return str(gmtime.tm_year) + '0' + str(gmtime.tm_mon) + '0' + str(gmtime.tm_mday)
        else:
            return str(gmtime.tm_year) + '0' + str(gmtime.tm_mon) + str(gmtime.tm_mday)
    else:
        if gmtime.tm_mday < 10:
            return str(gmtime.tm_year) + str(gmtime.tm_mon) + '0' + str(gmtime.tm_mday)
        else:
            return str(gmtime.tm_year) + str(gmtime.tm_mon) + str(gmtime.tm_mday)

def print_created_at_from_dict(data):
    try:
        for i in data:
            print(i['created_at'])
        return True
    except:
        print(' err: print_created_at_from_dict ')
        return False

def n_th_largest_value_from_list(n, list_in):
    try:
        i = 1
        while(i < n):
            list_in.remove(max(list_in))
            i += 1
        return max(list_in)
    except:
        return False

def open_n_more_files(number_of_file_loads, fileNames, unionData):
    i = 1
    while(i < number_of_file_loads):
        thisName = n_th_largest_value_from_list(2, fileNames)
        if thisName == False:
            break
        else:
            with open('database_json/' + thisName, 'r') as f:
                merge_without_duplicate(json.load(f), unionData)
                # print(len(unionData))
            i += 1

def exclude_objects_by_created_at(unionData, sortedData, gmtime):
    gmString = time.asctime(gmtime)
    if gmtime.tm_mday < 10:
        gmString = gmString[0:8] + '0' + str(gmtime.tm_mday)
    else:
        gmString = gmString[0:8] + str(gmtime.tm_mday)

    for obj in unionData:
        if gmString in obj['created_at']:
            sortedData.append(obj)
        else:
            pass
    return True
