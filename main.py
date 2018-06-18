# python3

import time
import json
import requests
from requests_oauthlib import OAuth1

from config import *
from credentials import *


# todo:
# .json file read and write

global tm_wday, tm_month, tm_mday, tm_clock, tm_zone, tm_year, struct_time


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


def main():
    print('icecandy...')
    # time.sleep(10)
    startTime = time.time()
    print( 'startTime:', time.asctime(time.localtime(startTime)) )

    for screen_name in userList:
        res = get_user_timeline(screen_name, count, exclude_replies, include_rts)
        for tweet in res:
            print(tweet['created_at'])
            tm_wday, tm_month, tm_mday, tm_clock, tm_zone, tm_year = tweet['created_at'].split()
            struct_time = time.strptime(tm_month, '%b')
            # print(str(struct_time.tm_mon)) # 6, month, int

            print(tweet['user']['screen_name'] + ' (' + tweet['user']['name'] + ')')
            print(tweet['full_text'])
            print('-----')
        # print(pjson(res))

    endTime = time.time()
    elapsedTime = endTime - startTime
    print('elapsedTime in sec: ' + str(elapsedTime))


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



# try: # 파일이 없으면 예외 발생
#     print('try: ' + symbol)
#     with open(symbol + '_' + str(period) + 'p_' + interval + '_candle.data', 'r') as f:
#         data = json.load(f)
#     print(len(data))
#
#     for i in data:
#         # print & write
#         with open(symbol + '_' + str(period) + 'p_' + interval + '_converted_data.txt', 'a') as f:
#             r = datetime.datetime.fromtimestamp(int(i[0]) / 1000).strftime('%Y-%m-%d %H:%M:%S' + ',')
#             rclosed = float(i[4])
#             f.write(r)
#             f.write(str(rclosed))
#             f.write('\n')
#
# except FileNotFoundError:
#     print('FileNotFoundError: ' + symbol)
#     pass



# try:
#     f = open('Estimated_BTC_Value.csv','a')
#     print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + ' ' + str(Estimated_BTC_Value) + ' BTC', file=f)
#
# except IOError as err:
#     print('File Error' + str(err))
# finally:
#     f.close()


if __name__ == "__main__":
    main()
