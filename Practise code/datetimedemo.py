import datetime

current_time= datetime.datetime.now()
print(current_time)
#print(current_time.day)
#print(current_time.year)
print(current_time.strftime("%H_%M_%S_%d_%m_%Y"))