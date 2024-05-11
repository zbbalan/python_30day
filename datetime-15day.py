###使用datetime模块获取当前时间
from datetime import datetime
print(dir(datetime))
#from datetime inport datetime
now = datetime.now()
print(now)
day = now.day
print(day)
year = now.year
print(year)
month = now.month
print(month)
hour = now.hour
print(hour)
minute = now.minute
print(minute)
print(f'{year}/{month}/{day}/{hour}:{minute}')
####初始化时间
new_year = datetime(2020,1,1,0,0,0)
print(new_year)
day = new_year.day
print(day)
year = new_year.year
print(year)
month = new_year.month
print(month)
hour = new_year.hour
print(hour)
minute = new_year.minute
print(minute)
print(f'{year}/{month}/{day}/{hour}:{minute}')

now = datetime.now()
t = now.strftime("%Y-%m-%d %H:%M:%S")
print(t)

