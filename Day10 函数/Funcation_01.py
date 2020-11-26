'''
 函数的定义与调用
    目的：函数的作用是增加代码的复用性,减少代码的冗余。

        def 函数名(参数,参数......):
            函数体
        调用：
            函数名(参数,参数......)
'''
import random


def generate_random():
    for i in range(10):
        ran = random.randint(1, 20)
        print(ran)


print(generate_random)  # 打印函数名 内存地址

# 调用函数：函数()  找到函数并执行函数体的内容
# 可以重复调用同个函数
generate_random()

print('----------------带参函数-----------------------')


def generate_random_01(number):  # 形参:形式上参数
    for i in range(number):
        rr = random.randint(1, 10)
        print(rr)


# 函数调用
generate_random_01(4)  # 实参：实际上的参数,具体的值

print('------------------------------------')


# 简易3次页面登录
def login(username, password):
    user = 'uzi'
    pas = '123456'
    for i in range(3):
        if user == username and pas == password:
            print('登录成功')
            break
        else:
            print('登录失败')
            username = input('请输入用户名:')
            password = input('请输入密码:')
    else:
        print('账号锁定！')


user = input('请输入用户名:')
pas = input('请输入密码:')
login(user, pas)
