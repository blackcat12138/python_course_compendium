'''
    time模块
'''
import calendar
import time

# 当前时间戳
t = time.time()
print(t)

# 延迟执行1秒钟
time.sleep(1)

t1 = time.time()
print(t1)

# 将时间戳转换成字符串
s = time.ctime(t)
print(s)

# 将时间戳转成元组方式
x = time.localtime(t)
print(x)
print(x.tm_hour)

# 将元组的转成时间戳
tt = time.mktime(x)
print(tt)

# 将时间戳转换成指定格式的字符串时间
y = time.strftime('%Y-%m-%d %H:%M:%S')
print(y)

# 将指定格式的字符串时间转换元组形式
r = time.strptime('2020/10/20', '%Y/%m/%d')
print(r)

print('-------------------------------')
# time模块中的三种时间形式
print('time stap:', time.time())  # 时间戳
print('local time：', time.localtime())  # struct_time类型的本地时间
print('utc time：', time.gmtime())  # struct_time类型的utc时间

# 三种时间形式间的转换
time_stamp = time.time()
loca_time = time.localtime(time_stamp)
utc_time = time.gmtime(time_stamp)
time_stamp_1 = time.mktime(loca_time)
time_stamp_2 = calendar.timegm(utc_time)
print(time_stamp, time_stamp_1, time_stamp_2)
