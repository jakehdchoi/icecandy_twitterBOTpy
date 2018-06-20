
import time
import requests

def convert_time_struct_into_yyymmdd_hhmmss_string(timeStruct):
    return str(timeStruct.tm_year) + two_digit_number_string_out(timeStruct.tm_mon) + two_digit_number_string_out(timeStruct.tm_mday) + '_' + two_digit_number_string_out(timeStruct.tm_hour) + two_digit_number_string_out(timeStruct.tm_min) + two_digit_number_string_out(timeStruct.tm_sec)

def two_digit_number_string_out(integer):
    if integer < 10:
        return '0' + str(integer)
    else:
        return str(integer)

print(convert_time_struct_into_yyymmdd_hhmmss_string(time.localtime()))

try:
    r = requests.get('http://www.google.com/nothere')
    print('try')
    print(type(r.status_code))
    print(r.json())
except:  # This is the correct syntax
    print('except')
    print(r.status_code)
    print(r.exceptions)

print('\n *successfully finished')

# try:
#     r = requests.get('http://www.google.com/nothere')
# except requests.exceptions.Timeout:
#     # Maybe set up for a retry, or continue in a retry loop
# except requests.exceptions.TooManyRedirects:
#     # Tell the user their URL was bad and try a different one
# except requests.exceptions.RequestException as e:
#     # catastrophic error. bail.
#     print e
#     sys.exit(1)
# except requests.exceptions.HTTPError as e:
#     print e
#     sys.exit(1)
