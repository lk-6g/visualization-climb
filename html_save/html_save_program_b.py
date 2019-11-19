# coding:utf-8
#导入 requests模块
import requests

#设置请求头,让网站监测是浏览器
headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3573.0 Safari/537.36',
}

# 爬取网页的URL
r = requests.get('http://www.liujiangblog.com/course/django/84')

#获取当前编码 当前编码有utf-8 ISO-8859-1
print(r.encoding)

# 新建一个文件名 例如：TencentHtml 设置文件格式编码为 utf-8
# 注意文件格式的编码和 获取的编码 要一致，不然出现乱码问题
file = "E:/Program Languag/Project/Eclipse/E-P/save/html/save.html"
with open(file, "w", encoding="utf-8") as f:
    for i in r.text:
        #将数据写入文件
        f.write(i)