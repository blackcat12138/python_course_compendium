'''
    递归函数：是普遍函数的一种表现形式,函数自己调用自己。
       特点:
'''


# 递归函数实现累加和
def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)


result = sum(10)
print(result)


# 递归函数没有终止点（无限循环）,会报递归错误
def f1(m):
    print('--------->', m)
    f1(m - 1)


f1(10)
