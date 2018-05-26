#_*_ coding:utf_8 _*_

import requests

from operator import itemgetter

#执行api调用并存储响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print 'Status code:',r.status_code  #输出

#处理每篇文章的信息
submission_ids = r.json() #获取一个包含hacker_news网ID的列表
submission_dicts = []  #创建一个存储热门文章信息的列表

#查询每个ID的具体信息
for submission_id in submission_ids[:30]:
    #获取每个ID的具体具体信息
    url = ('https://hacker-news.firebaseio.com/v0/item/'+
    str(submission_id)+'.json')  #根据id生成相应的api接口
    submission_r = requests.get(url)
    print 'Status code:',submission_r.status_code #检查是否链接成功
    response_dict = submission_r.json()  #生成一个包含ID信息的列表
    
    submission_dict = {
        'title':response_dict['title'],
        'link':'http://news.ycombinator.com/item?id='+str(submission_id),
        'comments':response_dict.get('descendants',0),
    }

    submission_dicts.append(submission_dict)  #将获取的信息存储到列表

submission_dicts = sorted(submission_dicts,key=itemgetter('comments'),reverse=False) #将获取到的类别内容以comments为关键词进行倒序排序

#逐个输出文章的相关信息
for submission_dict in submission_dicts:
    print '\nTitle:',submission_dict['title']
    print 'Discussion link:',submission_dict['link']
    print 'Comments:',submission_dict['comments']
