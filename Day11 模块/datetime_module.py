'''
    datetime模块是time模块的升级版,该模块底层封装了time模块

'''
import datetime
import time

# 获取时间
print(datetime.time.hour)  # 获取时间对象
print(time.localtime().tm_hour)

# 获取日期,因为date是类,所有要创建日期对象
d = datetime.date(2020, 10, 12)
print(datetime.date.day)
print(time.time())
print(datetime.date.ctime(d))  # 必须传值才能实现获取日期

print(datetime.date.today())  # 2020-11-16

# 计算时间差
timedel=datetime.timedelta(hours=2)
print(timedel)
now=datetime.datetime.now()
print(now)
res=now-timedel
print(res)
