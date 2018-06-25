# python3

import time
import json
import os


from functions import *


# todo:
# log file: implementation done, but need to be checked


print('icecandy..')
startTime = time.time() # secondes, used to calculate elapsedTime
gmtime = time.gmtime()

print( 'startTime(local) :', time.asctime(time.localtime(startTime)) )
print( 'startTime(global):', time.asctime(gmtime) )

# this is used to read and write a file
gmtimeString =  convert_time_struct_into_yyyymmdd_string(gmtime)

try:
    fileNames = os.listdir('database_json')
    maxFileName = max(fileNames)
except:
    print(' warn: database_json foler is empty ')

# todo: there must be a better way for this..
sortedData = []

# file load logic
try: # err if no file
    with open('database_json/' + gmtimeString + '.json', 'r') as f:
        try:
            unionData = json.load(f)
        except: # if not json format
            unionData = []
    # print(pjson(unionData))

    open_n_more_files(number_of_file_loads, fileNames, unionData)
    yesterdayCheck = False

except FileNotFoundError:
    print(" warn: There is no file that match, making an empty file.. ")
    with open('database_json/' + gmtimeString + '.json', 'w') as f:
        unionData = []
        json.dump(unionData, f)

    open_n_more_files(number_of_file_loads, fileNames, unionData)
    yesterdayCheck = True
    yesterdayGmtime = time.gmtime( time.time() - 60*60*24 )


def main():
    # collecting tweets --> unionData
    for screen_name in userList:
        res = get_user_timeline(screen_name, count, exclude_replies, include_rts)
        for tweet in res:
            print(tweet['created_at'])
            # print(convert_created_at_into_yyyymmdd_string(tweet['created_at']))
            print(tweet['user']['screen_name'] + ' (' + tweet['user']['name'] + ')')
            print(tweet['full_text'])
            print('-----')

        # print(len(unionData))
        # print(len(res))

        merge_without_duplicate(res, unionData)

    # yesterday file update logic
    while(yesterdayCheck == True):
        print('yesterday file updating..')
        try:
            with open('database_json/' + convert_time_struct_into_yyyymmdd_string(yesterdayGmtime) + '.json', 'r') as f:
                try:
                    yesterdayData = json.load(f)
                except:
                    yesterdayData = []
        except: # when no file exists
            yesterdayData = []

        merge_without_duplicate(yesterdayData, unionData)

        exclude_objects_by_created_at(unionData, yesterdayData, yesterdayGmtime)
        finalData = order_objects_by_created_at(yesterdayData)
        uniqueData = remove_duplicated_tweets_from_ordered_data(finalData)

        with open('database_json/' + convert_time_struct_into_yyyymmdd_string(yesterdayGmtime) + '.json', 'w') as f:
            json.dump(uniqueData, f)

        break


    print(len(unionData))
    exclude_objects_by_created_at(unionData, sortedData, gmtime)
    print(len(sortedData))
    finalData = order_objects_by_created_at(sortedData)
    print(len(finalData))
    uniqueData = remove_duplicated_tweets_from_ordered_data(finalData)
    print(len(uniqueData))

    with open('database_json/' + gmtimeString + '.json', 'w') as f:
        json.dump(uniqueData, f)



if __name__ == "__main__":
    main()
    endTime = time.time()
    elapsedTime = endTime - startTime
    print('elapsedTime in sec: ' + str(elapsedTime))
