#_*_ coding:utf_8 _*_

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

#执行api调用病存储调用信息
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)
print 'status code:',r.status_code

#将调用存储在一个变量中
response_dict = r.json()
print "Total repositories:",response_dict['total_count']

#探索有关仓库的信息
repo_dicts = response_dict['items']

#获取可视化数据
names,stars = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict["name"])
    stars.append(repo_dict["stargazers_count"])

#可视化
my_style = LS('#333366',base_style=LCS)
chart = pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)
chart.title = "Mosr-Starred python projects on GitHub"
chart.x_labels = names

chart.add("",stars)
chart.render_to_file('python_repos.svg')