# hashlib模块：加密算法 md5、sha256
import hashlib

# md5加密
msg = 'uiz你是sb'
md5 = hashlib.md5(msg.encode('utf-8'))
print(md5.hexdigest())

# base64网页小工具可以解码
# 加密的越长越安全

# sha1加密
sha253 = hashlib.sha1(msg.encode('utf-8'))
print(sha253.hexdigest())

# 模拟用户密码验证
password = '4396'
lists = []
shas = hashlib.sha256(password.encode('utf-8'))
lists.append(shas.hexdigest())

pwd = input('输入密码:')
shas = hashlib.sha256(pwd.encode('utf-8'))
pwd = shas.hexdigest()
print(pwd)
print(lists)
for i in lists:
    if pwd == i:
        print('登录成功')
