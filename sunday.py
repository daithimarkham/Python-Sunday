# David Markham, 2019-02-10
# Is it Sunday?

import datetime
import calendar
print("Is today Sunday?")

if datetime.datetime.today().weekday() == 6:
  print("Yay! It is Sunday.")
else:
  print("Unfortunately it is not Sunday.")

def findDay(date): 
    day, month, year = (int(i) for i in date.split(' '))     
    dayNumber = calendar.weekday(year, month, day) 
    days =["Monday", "Tuesday", "Wednesday", "Thursday", 
                         "Friday", "Saturday", "Sunday"] 
    return (days[dayNumber]) 
  
# Driver program 
print("Today is:")
date = '24 09 2019'
print(findDay(date))