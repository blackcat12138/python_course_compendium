'''
    __init__.py文件的讲解

    当导入包的时候,默认调用__init__.py文件中的内容
    作用:
        1.当导入包时,把一些初始化的函数,变量,类定义在__init__.py文件中
        2.此文件中函数,变量等的访问,只需要通过包名.函数....
        3.结合__all__=[通过*可以访问的模块]


    重点知识点
        from 模块 import * 与from 包 import * 两种导入方式的区别？
           from 模块 import *： 表示可以使用模块中的所有内容,若没有定义__all__所有的都可以访问,
                               但是若添加上__all__,只有__all__=['','']列表中元素可以访问的。
           from 包 import * ：表示该包中内容（模块）是不能访问,若想被访问则需在__init__.py文件中定义__all__=[可以通过*访问的模块]

'''
# 导入方式一
# import user  # --------------->user的__init__
# 导入方式二
# from user.models import User
# 调用init中的方法
# user.create_app()
# user.pring_A()

# 导入方式三
from user import *

user = models.User('admin', '4396')
user.show()

print(test.MAX)
