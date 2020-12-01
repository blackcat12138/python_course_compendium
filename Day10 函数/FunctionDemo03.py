'''
    开发登录验证
'''
import time

islogin = False


# 登录
def login():
    username = input('输入用户名：')
    password = input('输入密码：')
    if username == 'uzi' and password == '123456':
        return True
    else:
        return False


# 进行付款验证
def login_required(func):
    def wrapper(*args, **kwargs):
        global islogin
        print('------------付款---------')
        # 验证用户是否登录
        if islogin:
            func(*args, **kwargs)
        else:
            # 跳转到登录页面
            print('没有登录,不能付款！')
            islogin = login()
            print('result:', islogin)

    return wrapper


@login_required
def pay(money):
    print('正在付款,付款金额是：{}元'.format(money))
    print('付款中...')
    time.sleep(1)
    print('付款完成！')

# 调用
pay(1000)

pay(8000)
