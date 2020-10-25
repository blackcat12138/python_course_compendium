import datetime

# 计算300天前的今天是几号
now = datetime.datetime.now().date()  # datetime.date类型
delta = datetime.timedelta(days=300)
print(now - delta)
# 计算300天12小时前的时间
news = datetime.datetime.now()  # datetime.datetime类型
deltas = datetime.timedelta(days=300, hours=12)
print(news - deltas)
# 计算总天数和秒数、时间
print(datetime.timedelta(days=1, hours=2).days)
print(datetime.timedelta(days=1, hours=2).total_seconds())
print(datetime.datetime.now() + datetime.timedelta(days=-1))
print(datetime.datetime.now() - datetime.timedelta(days=1))
print(((datetime.datetime.now() + datetime.timedelta(days=1)) - datetime.datetime.now()).days)
