from bs4 import BeautifulSoup   #网页解析，获取数据
import re       #正则表达式，进行文字匹配
import urllib.request,urllib.error      #制定url，获取网页数据
import xlwt     #excel操作
import _sqlite3         #进行数据库操作
findpart1 = re.compile(r'<a href=".*">(.*?)</a>')
findscore = re.compile(r'<td class="bg_b">(.*?)</td>')
findpart2 = re.compile(r'<td>(.*?)</td>')
findG = re.compile(r'<td width="50">(.*?)</td>')
findT = re.compile(r'<td width="70">(.*?)</td>')
def main():
    baseurl = 'https://nba.hupu.com/stats/players/pts/'
    datalist = getData(baseurl)
    savepath = 'D:\\虎扑球员数据.xls'
    saveData(datalist,savepath)

def askURL(url):    #返回一页的源代码
    head = {'User-Agent':  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
    req = urllib.request.Request(headers=head,url=url)
    html = ''
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    return html

def getData(baseurl):
    datalist = []      #存储数据
    for i in range(1,4):
        url = baseurl + str(i)
        html = askURL(url)
        soup = BeautifulSoup(html,'html.parser')
        for item in soup.find_all('tr')[1:]:
            item = str(item)
            data = []       #保存一个球员的信息
            name = re.findall(findpart1,item)[0]          #抓取有用信息
            data.append(name)
            team = re.findall(findpart1,item)[1]
            data.append(team)
            score = re.findall(findscore,item)[0]
            data.append(score)
            l1 = re.findall(findpart2,item)[0]
            data.append(l1)
            l2 = re.findall(findpart2,item)[1]
            data.append(l2)
            l3 = re.findall(findpart2, item)[2]
            data.append(l3)
            l4 = re.findall(findpart2, item)[3]
            data.append(l4)
            l5 = re.findall(findpart2, item)[4]
            data.append(l5)
            l6 = re.findall(findpart2, item)[5]
            data.append(l6)
            G = re.findall(findG,item)[1]
            data.append(G)
            T = re.findall(findT,item)[0]
            data.append(T)
            datalist.append(data)
    return datalist
def saveData(datalist,savepath):
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('常规赛球员数据')
    col = ['球员','球队','得分','命中—出手','命中率','命中-三分','三分命中率','命中-罚球','罚球命中率','场次','上场时间']
    for i in range(11):
        sheet.write(0,i,col[i])
    for j in range(150):
        data = datalist[j]
        for k in range(11):
            sheet.write(j+1,k,data[k])
    book.save(savepath)
if __name__ == '__main__':
    main()









