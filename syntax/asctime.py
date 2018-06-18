# https://www.tutorialspoint.com/python/python_date_time.htm

import time

localtime = time.asctime( time.localtime(time.time()) )
print("Local current time : ", localtime)

# Local current time : Tue Jan 13 10:17:09 2009
