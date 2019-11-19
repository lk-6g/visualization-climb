# coding:utf-8

import urllib.request

# 爬取网页
def read_pageHtml(url):
    file = urllib.request.urlopen(url)
    data = file.read()
    return data

# 存储：方法一
def storageToLocalFiles(storagePath, data):
    fhandle = open(storagePath,"wb")
    fhandle.write(data)
    fhandle.close()
    
# 存储：方法二
def s(url, storagePath):
    urllib.request.urlretrieve(url, filename=storagePath)
    
url = "http://www.liujiangblog.com/course/django/84"
data = read_pageHtml(url)
storagePath = "E:/Program Languag/Project/Eclipse/E-P/save/html/save2.html"
storageToLocalFiles(storagePath, data)