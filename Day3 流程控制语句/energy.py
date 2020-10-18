'''
   模拟支付宝蚂蚁森林的能量产生过程
'''

while True:
    print("\n查询能量请输入能量来源！退出程序请输入0\n")
    print('能量来源如下:\n\n'
          '生活缴费、行走捐、共享单车、线下支付、网络购票\n')
    info = input()          # 获取控制台输入的内容
    print()                 # 换行
    if info == '生活缴费':   # 判断输入的能量来源
        print('180g')       # 打印对应的能量
    elif info == '行走捐':
        print('200g')
    elif info == '共享单车':
        print('80g')
    elif info == '线下支付':
        print('5g')
    elif info == '网络购票':
        print('80g')
    elif info == '0':
        print('已退出！')
        break
