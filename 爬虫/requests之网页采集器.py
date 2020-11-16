import requests

url = 'https://www.sogou.com/web?'
k = input('enter a word')
params = {'query':k}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'}
response = requests.get(headers = headers,url=url,params=params)
page_text = response.text
filename = k+'.html'
with open(filename,'w',encoding='utf-8') as fq:       #写入文件
    fq.write(page_text)
print('爬虫成功')