'''
    文件夹：主要放非py文件,比如：图片文件
        包：主要放py文件,其他放的是模块,可以存放多个模块,一个模块放多个类和函数

    项目>>包>>模块>>类 函数 变量

    articate包
        |--models.py
        |--__init__.py
        ....
    user包
        |--models.py
            |--User
        |--__init__.py
        |--test.py
        ....
    package.py

    导入包方式： from 包 import 模块
               from 包.模块 import 类|函数|变量
               from 包。模块 import *
'''
# 使用包中模块中的User类
# from user import models
#
# u=models.User('admin','123456')
# u.show()

from user.models import User

s = User('uzi', '4396')
s.show()

from articate.models import Articate

a = Articate('lpl总结', 'mlxg')
a.show()

from user.models import *

x = User('smlz', '753152')
x.show()

from  user.models import version

print(version)