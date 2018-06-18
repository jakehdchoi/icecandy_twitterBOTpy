# python3

import time
import json

from functions import *


# todo:


global tm_wday, tm_mon, tm_mday, tm_clock, tm_zone, tm_year, struct_time
global unionData


with open('database_json/example.json', 'r') as f:
    unionData = json.load(f)
print(len(unionData))


def main():
    print('icecandy...')
    # time.sleep(10)
    startTime = time.time()
    print( 'startTime:', time.asctime(time.localtime(startTime)) )

    for screen_name in userList:
        res = get_user_timeline(screen_name, count, exclude_replies, include_rts)
        for tweet in res:
            print(tweet['created_at'])
            tm_wday, tm_mon, tm_mday, tm_clock, tm_zone, tm_year = tweet['created_at'].split()
            struct_time = time.strptime(tm_mon, '%b')
            # print(str(struct_time.tm_mon)) # 6, month, int

            print(tweet['user']['screen_name'] + ' (' + tweet['user']['name'] + ')')
            print(tweet['full_text'])
            print('-----')

        # print(len(unionData))
        # print(len(res))

        DictListUpdate(res, unionData)


    endTime = time.time()
    elapsedTime = endTime - startTime
    print('elapsedTime in sec: ' + str(elapsedTime))


    with open('database_json/example.json', 'w') as f:
        json.dump(unionData, f)



if __name__ == "__main__":
    main()
