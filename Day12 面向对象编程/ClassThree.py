'''
    魔术方法
'''
from os.path import join


# class FileObject:
#     # 给文件对象进行包装从而确认在删除时文件流关闭
#     def __init__(self,filepath='~',filename='aa.txt'):
#         # 读写模式打开一个文件
#         self.file=open(join(filepath,filename),'r+')
#     def __del__(self):
#         self.file.close()
#         del self.file

class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
        # print("Product __init__gets called")

    # def __new__(cls, *args):
    #     new_product=object.__new__(cls)
    #     print("Product __new__ gets called")
    #     return new_product

    def __repr__(self):
        return f"Product({self.name!r},{self.price!r})"
    def __str__(self):
        return f"Product：{self.name},${self.price:.2f}"

product=Product("uzi",123)
repr(product)
evaluated=eval(repr(product))
type(evaluated)
