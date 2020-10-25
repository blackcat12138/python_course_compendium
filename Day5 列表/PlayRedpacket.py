import random
from decimal import Decimal

print('---------------微信抢红包------------------')
total = input('请输入要装入红包的总金额（元）：')
num = input('请输入红包的个数（个）:')
# 每个人最少能收到0.01元
min = 0.01
# 创建红包列表
money_list = []
total = Decimal(total)
num = Decimal(str(num))
min = Decimal(str(min))
# 判断红包金额是否大于每个红包个数*每个人最少获取的0.01
if total > num * min:
    # 根据循环到的红包个数 判断随机安全上限 不至于红包m没有没人最少0.01
    for i in range(1, int(num)):
        # 随机出 获取红包金额
        safe_total = (total - (num - i) * min)
        temp_min = min * 100
        temp_max = int(safe_total * 100)
        money = temp_min / 100 if temp_min > temp_max else (Decimal(random.randint(temp_min, temp_max))) / 100
        # 重置总金额 减去随机出的金额
        total -= money
        # 添加随机出的金额到 红包列表
        money_list.append(money)
    # 保存最后一个元素到红包数组 不足红包数量
    money_list.append(total)
    # 随机打乱列表顺序
    random.shuffle(money_list)
    for x in range(len(money_list)):
        print('第' + str(x + 1) + '个红包：' + str(money_list[x]) + '元')
