# 作者：ling-ly
# 开发时间：2023/2/18 16:12
import requests
url = "https://movie.douban.com/j/chart/top_list"
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'

}
# 重现封装参数
param = {
    "type": "25",
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20,
}
resp = requests.get(url,params=param,headers=header)   #get请求数据是params
# resp = requests.get(url,param)

print(resp.json())
# 没有数据可能被反爬了
# print(resp.request.headers)
# {'User-Agent': 'python-requests/2.28.2', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
# 查看请求头内数据User-Agent为'python-requests/2.28.2'不是浏览器
resp.close()    # 关闭连接，这很重要
