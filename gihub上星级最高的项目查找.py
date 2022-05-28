import requests
from plotly.graph_objs import Bar
from plotly import offline
#执行API调用并响应
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url,headers=headers)
print(f"Status code:{r.status_code}")
#姜API响应赋值给一个变量
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")
#探索仓库有关信息
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

#研究第一个仓库
repo_dict = repo_dicts[0]
for repo_dict in repo_dicts:
    print("\n有关每一个库的指定信息:")
    print(f"名称：{repo_dict['name']}")
    print(f"所有者：{repo_dict['owner']['login']}")
    print(f"星数：{repo_dict['stargazers_count']}")
    print(f"仓库网址：{repo_dict['html_url']}")
    print(f"创建时间：{repo_dict['created_at']}")
    print(f"更新时间：{repo_dict['updated_at']}")
    print((f"仓库描述：{repo_dict['description']}"))

