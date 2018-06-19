

import json
from operator import itemgetter


global unionData, sortedData

def pjson(a):
    return json.dumps(a, indent=2, sort_keys=True)



with open('database_json/20180619.json', 'r') as f:
    unionData = json.load(f)


for tweet in unionData:
    print(tweet['created_at'])
    print(tweet['user']['screen_name'] + ' (' + tweet['user']['name'] + ')')
    print(tweet['full_text'])
    print('-----')

print('')
print(len(unionData))


# # 날짜는 똑같고 시간만 비교하는 것이기 때문에, 이 함수를 쓸 수 있음
# # 날짜까지 다른 상태의 큰 데이터를 비교하려면 직접 함수를 구현해야 함
# unionData = sorted(unionData, key=itemgetter('created_at'), reverse=True)
#
#
# for tweet in unionData:
#     print(tweet['created_at'])
#     print(tweet['user']['screen_name'] + ' (' + tweet['user']['name'] + ')')
#     print(tweet['full_text'])
#     print('-----')
