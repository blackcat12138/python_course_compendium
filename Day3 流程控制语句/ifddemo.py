# 实例01 判断输入的是不是黄蓉所说的数
print("今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何？\n")
number = int(input("请输入您认为符合条件的数："))
if number % 3 == 2 and number % 5 == 3 and number % 7 == 2:
    print(number, '符合条件：三三数之剩二，五五数之剩三，七七数之剩二')

# 实例02
print("今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何？\n")
none = True
number = 0
while none:
    number += 1
    if number % 3 == 2 and number % 5 == 3 and number % 7 == 2:
        print("答曰：这个数是", number)
        none = False

# 实例03
print("今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何？\n")
for number in range(100):
    if number % 3 == 2 and number % 5 == 3 and number % 7 == 2:
        print("答曰：这个数是", number)

# 实例04
for i in range(1, 10):
    for j in range(1, i + 1):
        print(str(j) + 'x' + str(i) + '=' + str(i * j) + '\t', end='')
    print('')
