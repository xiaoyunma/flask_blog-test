import requests # 导入网页请求库
from bs4 import BeautifulSoup # 导入网页解析库

import urllib

# 传入URL
r = requests.get('https://www.baidu.com/')
r.encoding=r.apparent_encoding

text=r.text

# 解析URL
soup = BeautifulSoup(r.text, 'lxml')

a = soup.find_all('a')
for i in a:
    print(i)

