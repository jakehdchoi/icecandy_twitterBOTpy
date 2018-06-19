# python3

import time
import json
import os


from functions import *


# todo:
# unionData sort by created_at: collections.OrderedDict


print('icecandy...')
startTime = time.time()
gmtime = time.gmtime()

print( 'startTime(local) :', time.asctime(time.localtime(startTime)) )
print( 'startTime(global):', time.asctime(gmtime) )

gmtimeString =  convert_gmtime_into_NumString(gmtime) # this is used to open a file

fileNames = os.listdir('database_json')
maxFileName = max(os.listdir('database_json'))

# todo: there must be a better way for this..
sortedData = []

# file load logic
try: # err if no file
    with open('database_json/' + gmtimeString + '.json', 'r') as f:
        unionData = json.load(f)
    # print(pjson(unionData))

    open_n_more_files(number_of_file_loads, fileNames, unionData)

except FileNotFoundError:
    print(" There is no file that match, so let's make an empty file. ")
    with open('database_json/' + gmtimeString + '.json', 'w') as f:
        unionData = []
        json.dump(unionData, f)

    open_n_more_files(number_of_file_loads, fileNames, unionData)



def order_objects_by_created_at(unionData):
    pass

def main():
    # time.sleep(10)
    for screen_name in userList:
        res = get_user_timeline(screen_name, count, exclude_replies, include_rts)
        for tweet in res:
            print(tweet['created_at'])
            # print(convert_created_at_into_NumString(tweet['created_at']))
            print(tweet['user']['screen_name'] + ' (' + tweet['user']['name'] + ')')
            print(tweet['full_text'])
            print('-----')

        # print(len(unionData))
        # print(len(res))

        merge_without_duplicate(res, unionData)

        # todo: sort by created_at

        exclude_objects_by_created_at(unionData, sortedData, gmtime)

        finalData = order_objects_by_created_at(unionData)
    print(pjson(sortedData))
    # with open('database_json/' + gmtimeString + '.json', 'w') as f:
    #     json.dump(unionData, f)



if __name__ == "__main__":
    main()
    endTime = time.time()
    elapsedTime = endTime - startTime
    print('elapsedTime in sec: ' + str(elapsedTime))
