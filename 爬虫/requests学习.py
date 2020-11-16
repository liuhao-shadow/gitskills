import requests
# requests模块的使用:
#         指定url
#         发起请求
#         响应数据
#         存储数据

url = 'https://www.sogou.com/'
response = requests.get(url = url)        #获取到的是字符串
html = response.text
print(html)

