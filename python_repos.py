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

#研究所有仓库
print "Slected information about first repository:"
for repo_dict in repo_dicts:
    print "\nname:",repo_dict["name"]
    print "Owner:",repo_dict["owner"]["login"]
    print "Start:",repo_dict["stargazers_count"]
    print "Repository:",repo_dict["html_url"]
    print "Created",repo_dict["created_at"]
    print "Updated:",repo_dict["updated_at"]
    print "Description:",repo_dict["description"]