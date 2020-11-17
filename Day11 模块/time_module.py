'''
    time模块
'''
import time

# 当前时间戳
t = time.time()
print(t)

# 延迟执行3秒钟
time.sleep(3)

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
