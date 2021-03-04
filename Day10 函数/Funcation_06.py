'''
    变量的作用域
'''
# 局部变量中的global关键字
g_b =2
def t1():
    global  g_b
    g_b=3
t1()
print(g_b)

