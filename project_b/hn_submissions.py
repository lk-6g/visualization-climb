import requests, pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code: ", r.status_code)

submission_ids = r.json()

titles, plot_dicts =[],[]
for submission_id in submission_ids:
    url = 'https://hacker-news.firebaseio.com/v0/' + str(submission_id) + '.json'
    submission_r = requests.get(url)
    print("Submission Statu code: ", submission_r.status_code)
    
    reponse_dict = submission_r.json()
    titles.append(reponse_dict['title'])
    
    plot_dict = {
        'value':reponse_dict.get('descendants', 0),
        'label':reponse_dict['id'],
        'xlink':url}
    plot_dicts.append(plot_dict)
    
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size =24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Hacker-News'
chart.x_labels = titles

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')