'''
    函数中的返回值与局部变量、全局变量
        返回值：将函数中运算的结果通过return关键字返回出来。
                返回出来的结果需要通过变量进行接收才有意义。
            1.return后面可以是一个参数也可以是多个参数,底层会将多个参数先放在一个元组中,
                若通过一个参数接收,则将以元组作为整体   x=add(1,2) x-->(1,2,3)
                若通过多个参数接受,则以原样输出
            2.return后面的参数与接收的变量个数必须一致,可以用一个变量接收多个参数。
        局部变量：函数内部声明的变量,仅限于在函数内部中使用(修改与访问)。
        全局变量：定义在函数外部的变量,所有函数都可以访问,
                 只能通过global关键字声明全局变量后才能够修改,
                 修改后的变量可以让所有函数进行访问。
        变量的优先级：局部变量与全局变量同名优先访问修改局部变量,(谁近访问谁)。
            当全局变量是不可变时,比如：字符串、元组、布尔,在函数中需要修改就需要加global关键字;
            当全局变量是可变时,比如：列表、字典,在函数中修改可以无需通过global关键字进行声明。

'''
import random


def add(x, y):
    return x + y


c = add(1, 2)
print(c)


def ayy(t, l, e):
    return 'hello', 'world'


y, z = ayy(1, 3, 4)
print(z, y)

print('---------------------------')
# 练习：加入到购物车
# 用于判断用户是否登录变量 默认是没有登录的
islogin = False


# 输入验证码 封装成一个函数
def generate_checkcode(n):
    x = '01234dfdagaerwerynd'
    code = ''
    for i in range(n):
        ran = random.randint(0, len(x) - 1)
        code += x[ran]
    return code


# 添加商品
def add_shoppingcart(goodsName):
    global islogin
    if islogin:
        if goodsName:
            # 登录的
            print('成功将{}加入到购物车中！'.format(goodsName))
        else:
            print('没有选中商品！')
    else:
        # 没登录
        answer = input('用户没有登录！是否登录用户?(yes/no)')
        if answer == 'yes':
            username = input('输入用户名：')
            password = input('输入密码：')
            code = input('输入验证码：')
            #  在一个函数内调用另一个函数
            islogin = login(username, password, code)
            print('islogin状态:', islogin)
        else:
            print('不能添加任何商品！')


# 登录验证
def login(username, password, code):
    cc = generate_checkcode(5)
    if username == 'uzi' and password == '123456' and cc.lower() == code.lower():
        # 登录成功
        # print('登录成功')
        # print('验证码输入正确')
        return True
    else:
        # print('用户名或密码有误')
        return False


# 调用函数：添加商品到购物车中
username = input('输入用户名：')
password = input('输入密码：')
code = input('输入验证码：')
islogin = login(username, password, code)

add_shoppingcart('vn皮肤')
