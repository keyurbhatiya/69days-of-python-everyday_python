# create a python alarm clock using datetime 

# python date time module

import datetime
import time
# get alarm tim from user


alarm_hour = int(input("Enter alarm hour(24 hour format): "))

alram_minute = int(input("Enter alarm minute : "))

print("Alarm is set sucess!")

while True:
    now = datetime.datetime.now()
    current_hour = now.hour
    current_minute = now.minute

    print("Current time : ", now.strftime("%H:%M:%S"))

    if current_hour == alarm_hour and current_minute == alram_minute:
        print("Alarm Ringing !! Wake Up!")
        break

    time.sleep(10) # check every 10 sec


print("ENd of day 21")


timedelta(days=1) (Glowing)