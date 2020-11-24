'''
    初次使用urllib实现爬虫的数据请求
        urllib.request.urlopen(url)：发起get请求
        urllib.parse.quote()：将中文进行url编码
        urllib.request.urlretrieve(url,filename)：下载url保存到filename
'''
from urllib.request import urlopen,urlretrieve
from urllib.parse import quote

import ssl
ssl._create_default_https_context=ssl._create_unverified_context

def search_baidu(wd='千峰'):
    # 网络资源的接口(URL)
    url='https:/www.baidu.com/s?wd=%s'
    response=urlopen(url % quote(wd))
    assert response.code==200
    print('请求成功')

    # 读取响应的数据
    bytes=response.read()

    # 当对象jin' with open() as file:


if __name__ == '__main__':
    search_baidu()

