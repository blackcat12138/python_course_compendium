# 方法 打印演员开始出演这个剧本
print("==============案例一================")


def Scrip(lead):
    print(lead + '开始参演这个剧本')


# 获取控制台输入的演员姓名
Lead = input('导演选定的主角是：')
Scrip(Lead)

print("=============案例二=================")
num = (i for i in range(3))
print(num.__next__())
print(num.__next__())
print(num.__next__())
nums = tuple(num)
print("转换后：", nums)

print("===============案例三===============")


def Package_pice(Package1, Package2, Package3):
    print(Package1 + '13元')
    print(Package2 + '9.9元')
    print(Package3 + '20元')


Package1 = '考神套餐'
Package2 = '单人套餐'
Package3 = '情侣套餐'
print('米线店套餐如下：1.' + Package1 + ' 2.' + Package2 + " 3." + Package3)
Package_pice(Package1, Package2, Package3)
