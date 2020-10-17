'''
    1.input()：不换行键盘输入内容
    2.python中的变量初始默认为None
'''
print('欢迎使用XXX充值业务，请输入充值金额：')
info = input()
print('充值成功，您本次充值', info, '元')

# ------------------
father = None
mother = None
print('请输入父亲的身高：')
father = input()
print('请输入母亲身高：')
mother = input()
print('预测儿子身高为：', (float(father) + float(mother)) * 0.54)

# ------------------
print('请输入当天行走的步数！')
step = input()
calorie = int(step) * 28
print('今天共消耗卡路里：', calorie, "(即", calorie / 1000, "千卡)")
