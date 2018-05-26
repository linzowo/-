#_*_ coding:utf_8 _*_

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

#解决无法处理字符流的问题
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#执行api调用病存储调用信息
url = 'https://api.github.com/search/repositories?q=language:C&sort=stars'

r = requests.get(url)
print 'status code:',r.status_code

#将调用存储在一个变量中
response_dict = r.json()
print "Total repositories:",response_dict['total_count']

#探索有关仓库的信息
repo_dicts = response_dict['items']

#获取可视化数据
names,plot_dicts = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict["name"])

#添加星星数和简介
    plot_dict = {
        'value':repo_dict['stargazers_count'],
        'label':str(repo_dict['description']),
        'xlink':repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)

#可视化
my_style = LS('#333366',base_style=LCS)

my_config = pygal.Config() #创建一个config类的实例
my_config.x_label_rotation = 45 #将x标签沿着x轴旋转45度
my_config.show_legend = False  #隐藏图例
my_config.title_font_size = 24  #标题的大小
my_config.label_font_size = 14 #副标签的字体大小
my_config.major_label_font_size = 18  #主标签的字体大小
my_config.truncate_label = 15 #控制标签的显示长度在15个字节内
my_config.show_y_guides = False #将y轴的水平线隐藏
my_config.width = 1000  #设置图表的尺寸

chart = pygal.Bar(my_config,style=my_style)
chart.title = "Mosr-Starred python projects on GitHub"
chart.x_labels = names

chart.add("",plot_dicts)
chart.render_to_file('C_repos.svg')