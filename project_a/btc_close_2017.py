# coding: utf-8

import json, pygal, math
from itertools import groupby

filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)
    
dates, months, weeks, weekdays, close = [], [], [], [], []
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))
    
# 收盘价折线图
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价 (￥)'
line_chart.x_labels = dates
line_chart.x_labels_major = dates[::20]
line_chart.add('收盘价 (￥)', close)
line_chart.render_to_file('收盘价折线图 (￥).svg')

# 收盘价对数折线图
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价对数变换(￥)'
line_chart.x_labels = dates
line_chart.x_labels_major = dates[::20]
close_log = [math.log10(_) for _ in close]
line_chart.add('log收盘价 (￥)', close_log)
line_chart.render_to_file('收盘价对数变换折线图 (￥).svg')

def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _:_[0]):
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title + '.svg')
    return line_chart

# 收盘价日均值
idx_month = dates.index('2017-12-01')
draw_line(months[:idx_month], close[:idx_month], '月收盘价日均值（￥）', '日均值')

# 收盘价周均值
idx_week = dates.index('2017-12-11')
draw_line(weeks[1:idx_week], close[1:idx_week], '周收盘价日均值（￥）', '日均值')

# 星期收盘价均值
idx_weekday = dates.index('2017-12-11')
wd = ['Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday', 'Sunday']
weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_weekday]]
line_chart_weekday = draw_line(weekdays_int, close[1:idx_weekday], '星期收盘价均值（￥）', '星期均值')
line_chart_weekday.x_labels = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line_chart_weekday.render_to_file('星期收盘价均值（￥）.svg')

# 收盘价仪表盘
with open('收盘价Dashboard.html', 'w', encoding='utf8') as html_file:
    html_file.write('<html><head><title>收盘价Dashboard</title><metacharset="utf-8"><head><body>\n')
    for svg in ['收盘价折线图 (￥).svg', '收盘价对数变换折线图 (￥).svg', '月收盘价日均值（￥）.svg',
                '周收盘价日均值（￥）.svg', '星期收盘价均值（￥）.svg']:
        html_file.write('    <object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))
        html_file.write('</body></html>')
    