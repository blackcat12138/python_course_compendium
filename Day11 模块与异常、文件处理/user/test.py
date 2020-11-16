# 用户发表文章
from articate.models import Articate
from user.models import User
# from .models import User # 当前目录下的models中的User类

from calculate import add

# user是通过User类导入创建的
user = User('sofm', '4396')

art = Articate('lpl的个人总结', 'sofm')
user.publish_article(art)

lists = [2, 3, 45, 6, 2]
res = add(*lists)
print(res)
