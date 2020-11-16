import requests
import json
url = 'https://fanyi.baidu.com/sug'
word = input('enter a word')
data = {
    'kw':word
}
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'}

response = requests.post(url=url,data=data,headers=headers)
result = response.json()     #需要确认响应的数据是json类型
filename = word+'.json'
fq = open(filename,'w',encoding='utf-8')
json.dump(result,fp=fq,ensure_ascii=False)
print('爬虫成功')

