#_*_ coding:utf_8 _*_

import requests

#执行api调用病存储调用信息
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)
print 'status code:',r.status_code

#将调用存储在一个变量中
response_dict = r.json()
print "Total repositories:",response_dict['total_count']

#探索有关仓库的信息
repo_dicts = response_dict['items']
print "Repositories returned:",len(repo_dicts)

#研究第一个仓库
repo_dict = repo_dicts[0]
print "\nkeys:",len(repo_dict)
for key in sorted(repo_dict.keys()):
    print key
