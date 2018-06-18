# python3

import time
import json
import os


from functions import *


# todo:
# filename according to the data
# unionData sort by created_at: collections.OrderedDict


print('icecandy...')
startTime = time.time()
print( 'startTime(local):', time.asctime(time.localtime(startTime)) )

gmtime = convert_gmtime_into_NumString()
FileNames = max(os.listdir('database_json'))
# print(FileNames)

try: # err if no file
    with open('database_json/' + gmtime + '.json', 'r') as f:
        unionData = json.load(f)
    # print(pjson(unionData))
    # open 2 more
except FileNotFoundError:
    print('FileNotFoundError')
    # make one && open 2 more
    pass


# def main():
#     # time.sleep(10)
#     for screen_name in userList:
#         res = get_user_timeline(screen_name, count, exclude_replies, include_rts)
#         for tweet in res:
#             print(tweet['created_at'])
#             # print(convert_created_at_into_NumString(tweet['created_at']))
#             print(tweet['user']['screen_name'] + ' (' + tweet['user']['name'] + ')')
#             print(tweet['full_text'])
#             print('-----')
#
#         # print(len(unionData))
#         # print(len(res))
#
#         merge_without_duplicate(res, unionData)
#
#         # todo: sort by created_at
#
#     with open('database_json/' + gmtime + '.json', 'w') as f:
#         json.dump(unionData, f)
#
#     endTime = time.time()
#     elapsedTime = endTime - startTime
#     print('elapsedTime in sec: ' + str(elapsedTime))
#
#
#
#
# if __name__ == "__main__":
#     main()
