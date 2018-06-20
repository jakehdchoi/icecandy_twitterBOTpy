# python3

import time
import json
import os


from functions import *


# todo:
# when the date changes, check the previous file if it has all the data


print('icecandy...')
startTime = time.time()
gmtime = time.gmtime()

print( 'startTime(local) :', time.asctime(time.localtime(startTime)) )
print( 'startTime(global):', time.asctime(gmtime) )

gmtimeString =  convert_gmtime_into_NumString(gmtime) # this is used to open a file

try:
    fileNames = os.listdir('database_json')
    maxFileName = max(fileNames)
except:
    print(' err: database_json foler is empty ')

# todo: there must be a better way for this..
sortedData = []

# file load logic
try: # err if no file
    with open('database_json/' + gmtimeString + '.json', 'r') as f:
        try:
            unionData = json.load(f)
        except:
            unionData = []
    # print(pjson(unionData))

    open_n_more_files(number_of_file_loads, fileNames, unionData)

except FileNotFoundError:
    print(" There is no file that match, so let's make an empty file. ")
    with open('database_json/' + gmtimeString + '.json', 'w') as f:
        unionData = []
        json.dump(unionData, f)

    open_n_more_files(number_of_file_loads, fileNames, unionData)



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
