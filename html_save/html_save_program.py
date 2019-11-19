# coding:utf-8
import requests

def get_html(pages, file):
    print("page ", i, ": ", pages.encoding)

    with open(file, "w", encoding="utf-8") as f:
        for page in pages.text:
            f.write(page)

headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3573.0 Safari/537.36',
}

for i in range(0, 44):
    pages = requests.get('https://github.com/stacklens/django_blog_tutorial/blob/master/md/' + str(1) + '.*' + '.md')
    file = "E:/Program Languag/Project/Eclipse/E-P/html_save/html/" + str(i) + ".html"

    get_html(pages, file)