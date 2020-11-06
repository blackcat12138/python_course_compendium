'''
    字符串的运算符：+、*
'''
s1 = 'abc'
s2 = "abc"
s3 = s1 + s2  # +相当于拼接符
s4 = s1 * 5  # *倍数
print(s3)
print(s4)

# in 在..里面,返回布尔类型 True、False
name = 'steven'
result = 'st' in name
print(result)

# % 字符串的格式化
print('%s说:%s' % (name, '大家好好学习！'))
# r 保留原格式 有r则不发生转义,没有r则发生转义(例：\)
print(r'我\'哈哈哈')

# 通过切片实现字符串的倒序
# [::]
str1 = 'adcefghj'
print(str1[::-1])  # jhgfecda


