'''
   猜数字游戏
    编写一个猜数字的小游戏，随机生成一个1到10之间（包括1和10）的数字作为基准数，
    玩家每次通过键盘输入一个数字，
    如果输入的数字和基准数相同，则成功过关，否则重新输入。如果玩家输入-1，则表示退出游戏。
'''
import random

print('\n——————猜数字游戏——————\n')
random = random.randint(1, 10)
print("请输入1~10之间的任意一个数：")
while True:
    guess = input()
    # 若猜测的数字小于基准数，则提示用户输入的数太小，并让用户重新输入
    if int(guess) != 0 and int(guess) < random:
        print('太小，请重新输入：')
    # 若猜测的数字大于基准数，则提示用户输入的数太大，并让用户重新输入
    elif int(guess) != 0 and int(guess) > random:
        print('太大，请重新输入：')
    # 输入的数字与随机数相同时，用户猜对数字，获得成功，游戏结束
    elif int(guess) == random:
        print('恭喜你，你赢了，猜中的数字是：', random)
        print('\n———————游戏结束———————')
        break
    # 若输入的数字是0，循环结束的原因是用户选择退出游戏
    elif guess == '0':
        print('退出游戏！')
        break
