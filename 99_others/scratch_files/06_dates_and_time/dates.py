#################################### DateType ####################################
from datetime import datetime

date_in_string = "06/11/2016"
datetime.strptime(date_in_string, "%m/%d/%Y") # string previously time

now = datetime.now()
now # class is datetime.datetime

today = datetime.today() # same as now()
today # class is datetime.datetime 

current_time_string = datetime.strftime(now, "%m/%d/%Y") # string from time
current_time_string # class is string
now 
str(now) # works too

# components
# d, m, y, h, m, s(decimal allowed)

# standard formats
now.isoformat() # ISO format - widely used

#################################### Containers ####################################
my_dates = ["2020 11 21", "2020 11 20", "2020 11 22"]
# datetime.strptime(my_dates, "%m/%d/%Y") # list not allowed, string expected
my_dates = [datetime.strptime(x, "%Y %m %d") for x in my_dates]
my_dates 
sorted(my_dates) # sorting allowed

#################################### Extractions ####################################
now.year
now.month
now.day
now.hour
now.minute
now.second
now.weekday() # 0 for monday

import calendar
calendar.day_name[0] # Monday
calendar.day_name[now.weekday()] # Monday

############ Manipulations ############
from datetime import timedelta
time_additions = timedelta(days=20)
time_additions # class: datetime.timedelta
# days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0

now + timedelta(days=1, weeks=1) # add 1 days plus 1 weeks
now + timedelta(days=8, weeks=1) # add 8 days plus 1 weeks 

now - timedelta(days=20)
now + timedelta(days=20)

time_1 = now
time_2 = now + timedelta(minutes=60)

time_2 - time_1 # 3600 seconds. Class:datetime.timedelta
(time_2 - time_1).seconds # 3600
(time_2 - time_1).days # 0
(time_2 - time_1).microseconds # 0
(time_2 - time_1).milliseconds # not applicable
(time_2 - time_1).minutes # not applicable
(time_2 - time_1).hours # not applicable
(time_2 - time_1).weeks # not applicable

(time_2 - time_1).total_seconds() # 3600.0

(time_2 - time_1).total_seconds() /60 # total minutes = 60.0
# or 
(time_2 - time_1)/timedelta(minutes=1) # total minutes = 60.0


time_1 - time_2
(time_1 - time_2).seconds # 82800
(time_1 - time_2).days # -1
(time_1 - time_2).microseconds # 0
(time_1 - time_2).milliseconds # not applicable
(time_1 - time_2).minutes # not applicable
(time_1 - time_2).hours # not applicable
(time_1 - time_2).weeks # not applicable
(time_1 - time_2).total_seconds() # -3600.0

# date range generate
from datetime import timedelta
[now + timedelta(days = x+1) for x in range(3)]
# now + [timedelta(days = x+1) for x in range(3)] # vectorization not allowed

my_date_ranges = [now + timedelta(days = x+1) for x in range(10)]
min(my_date_ranges)
max(my_date_ranges)

#################################### Modifications ################################################
# replace a component of datetime object
# now.day = 1 # fails
now.replace(day=1) # returns a value and not modify inplace

#################################### Extras ################################################
# 2 digit convert to 4 digit year
# Cutoff: 1969 Jan 01
datetime.strptime("2020 12 31", "%Y %m %d") # 2020
datetime.strptime("91 12 31", "%y %m %d") # 1991
[datetime.strptime(f"{str(x).zfill(2)} 12 31", "%y %m %d") for x in range(0,100,1)]
[datetime.strptime(f"{str(x).zfill(2)} 01 01", "%y %m %d") for x in range(0,100,1)]

#################################### Timezones ####################################
import pytz

#################################### pendulum library ####################################
import pendulum

