'''
    在python中,模块是代码组织的一种方式,把功能相近的函数放在一个文件中,
    一个文件(.py)就是一个模块(module),模块名就是文件名去掉后缀py。这样做的好处是：
        (a).提高代码的复用性,可维护性。模块编写完成后,方便其他项目导入
        (b).解决命名冲突,不同模块中相同的命名不会冲突

    1.自定义模块
    2.使用系统一些模块

    3.导入模块的方式：
        (a).import 模块名
            访问的方式 模块名.变量 模块名.函数 模块名.类
        (b).from 模块名 import 变量|函数|类
            在代码中可以直接使用变量, 函数, 类
        (c).from 模块名 import *
            调用模块中所有内容
            若想限制获取的内容,所以在模块中使用__all__=[使用*可以访问的元素]
     4.无论是import还是from的形式,都会将模块内容进行加载
        若不希望其进行调用.就会用到__name__
        在自己的模块中__name__叫：__main__
        如果在其他模块中通过导入方式调用的话：__name__:模块名

'''
from calculate import add

lists = [4, 2, 3, 1, 4, 5]

# 导入模块方式一
# 导入模块 import 模块名
# import calculate
#
# # 使用模块中的函数 模块名.变量 模块名.函数 模块名.类
# result = calculate.add(*lists)
# print(result)
#
# # 使用模块变量
# print(calculate.number)
#
# # 使用模块中的类
# cal = calculate.Calculate(88)
# cal.test()
#
# calculate.Calculate.test1()

# 导入模块方式二
# from calculate import add,number,Calculate
#
# result=add(*lists)
# print(result)
#
# sum=result+number
# print(sum)
#
# c=Calculate(80)
# c.test()

# 导入模块方式三
from calculate import *

result = add(*lists)
print(result)
