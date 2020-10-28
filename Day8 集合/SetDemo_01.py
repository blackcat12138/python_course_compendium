
# add()：向集合中添加类型元素
ls=set(['java','python','shell','scale'])
ls.add('go')
print(ls)
# update()：将添加的元素拆分成字符,添加到集合中。
ls.update('Android')
print(ls)
# remove()：删除集合中的元素,若不存在则报错。
ls.remove('java')
print(ls)
#ls.remove('c++')
#print(ls)
# discard()：删除集合中的元素,不存在报错。
ls.discard('c++')
print(ls)
# pop()：删除一个元素,并返回这个元素。
ls.pop()
print(ls)
# clear()：清空集合中的所有元素。
ls.clear()
print(ls)