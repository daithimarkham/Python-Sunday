# David Markham, 2019-02-10
# Is it Sunday?

import datetime

if datetime.datetime.today().weekday() == 6:
  print("Yay! It is Sunday.")
else:
  print("Unfortunately it is not Sunday.")
