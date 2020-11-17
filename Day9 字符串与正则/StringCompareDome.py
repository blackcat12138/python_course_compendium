'''
    字符串串的三种不同符号的比较
'''
s1 = 'abc'
s2 = "abc"
s3 = '''
abc
'''
# 输出结果：2440169588360 2440169588360 2440169637680
# 三引号占用的内存空间与单双引号的不同（前提是三引号不在一行上）
print(id(s1), id(s2), id(s3))

print(s1 == s2)  # 比较的是内容
print(s1 is s2)  # 比较的是地址

print(s2 == s3)
print(s2 is s3)

print(s2)
print(s3)

s1 = input('请输入：')  # 'abc'
s2 = input('请输入：')  # 'abc'

print(s1 == s2)  # True
print(s1 is s2)  # False
'''
结论:
    常量赋值is是True,input输入底层做了处理所以最后的地址是不一样的
'''
