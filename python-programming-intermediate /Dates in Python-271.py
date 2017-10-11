## 1. The Time Module ##

import time

current_time = time.time()
print(current_time)

## 2. Converting Timestamps ##

import time
current_time = time.time()
current_struct_time = time.gmtime(current_time)
current_hour = current_struct_time.tm_hour
print(current_hour)

## 3. UTC ##

import datetime
current_datetime = datetime.datetime.utcnow()
current_year = current_datetime.year
current_month = current_datetime.month
print(current_datetime)

## 4. Timedelta ##

import datetime
kirks_birthday = datetime.datetime(day = 22, month = 3, year = 2233 )
diff = datetime.timedelta( weeks = 15 )
before_kirk = kirks_birthday - diff
print(before_kirk)

## 5. Formatting Dates ##

import datetime

mystery_date_formatted_string = mystery_date.strftime("%I:%M%p on %A %B %d, %Y")

## 6. Parsing Dates ##

import datetime
mystery_date = datetime.datetime.strptime(mystery_date_formatted_string,"%I:%M%p on %A %B %d, %Y")
print(mystery_date)

## 8. Reformatting Our Data ##

import datetime
for val in posts:
    val[2] = datetime.datetime.fromtimestamp(float(val[2]))
    

## 9. Counting Posts from March ##

march_count = 0
for post in posts:
    if post[2].month == 3:
        march_count = march_count + 1
        

    
    

## 10. Counting Posts from Any Month ##

def post_counter(month):
    count = 0
    for row in posts:
        if row[2].month == month :
            count += 1
    return count

feb_count = post_counter(2)
aug_count = post_counter(8)
