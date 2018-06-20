# https://docs.python.org/3/library/time.html

import time

# From                        To	                        Use
# seconds since the epoch	    struct_time in UTC	        gmtime()
# seconds since the epoch	    struct_time in local time	localtime()
# struct_time in UTC	        seconds since the epoch	    calendar.timegm()
# struct_time in local time	    seconds since the epoch	    mktime()

# current gmtime
print(time.asctime(time.gmtime()))
# yesterday gmtime
print(time.asctime(time.gmtime( time.time() - 60*60*24 )))
