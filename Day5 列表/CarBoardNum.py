# 初始化号牌列表
carNum = ["津A·12345", "沪A·23456", "京A·34567"]
# 根据列表元素个数循环列表
for i in range(len(carNum)):
    # 提示用户输出的是第几个车牌
    print('第' + str(i + 1) + '张车牌号码：')
    # 输出车牌
    print(carNum[i])
    # 获取字符串第一个字符 判断归属地
    if carNum[i][0] == '津':
        # 输出车牌归属地
        print('这张号牌的归属地：天津')
    if carNum[i][0] == '沪':
        print('这张号牌的归属地：上海')
    if carNum[i][0] == '京':
        print('这张号牌的归属地：北京')
