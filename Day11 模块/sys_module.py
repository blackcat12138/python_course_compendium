'''
    当导入一个模块,python解析器对模块位置的搜索顺序是:
        1.当前目录
        2.若不在当前目录,python则搜索在shell变量PYTHONPATH 下的每个目录。
        3.若都找不到,python会查看默认路径.UNINX下,默认路径一般为/usr/local/lib/python/
           模块搜索路径存储在system模块的sys.path变量中。
           变量中包含当前目录.PYTHONPATH和由安装过程决定的默认目录。
'''

import sys

'''
    自定义模块
    系统模块：sys模块
'''

print(sys.path)

print(sys.version)

# 运行程序时的参数,argv是一个列表
print(sys.argv)
