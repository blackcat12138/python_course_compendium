'''
    练习：hello world
        逆序输出world:-->dlrow
        正向输出hello
        逆序输出整个hello world
        打印获取oll
        打印llo wo
    切片总结:
        str[start:end:方向和步长]
        方向： 1 表示从左向右 0，1，2，3，4，5...
              -1  表示从右到左 5，4，3，2，1
             注意：数值的顺序

'''
s1='hello world'
print(s1[-1:-6:-1])

print(s1[:5])

print(s1[::-1])

print(s1[4:1:-1])

print(s1[2:-3]) # s1[2:8]