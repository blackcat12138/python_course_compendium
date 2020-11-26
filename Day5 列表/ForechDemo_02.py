'''
    遍历列表元素
    enumerate()：实现同时输出索引值和元素内容。
            num=[7,23,43,22,33,2]
            for index,item in enumerate(num):
                print(index+1,item)
'''
s=[1,2,3,4,6,7,9]

# 遍历方式一:
for i in s:
    print(i)

# 遍历方式二：
print('===========================')
for index,i in enumerate(s):
    print(index,i)
print(enumerate(s))

list1=[]
index=0
print('============================')
for i in s:
    t1=(index,i)
    list1.append(t1)

    index+=1
print(list1)

print('-----------------------------')
for index,value in list1:
    print(index,value)
