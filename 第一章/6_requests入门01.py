# 作者：ling-ly
# 开发时间：2023/2/18 14:49
# 安装requests
# pip install requests

import requests
quest = input("输入你想要的内容\n")
url = f"https://www.sogou.com/web?query={quest}"    # get方式可直接拼接，post不行
# 反爬伪装，给请求头中的User-Agent(设备）
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}
resp = requests.get(url,headers=headers)   # get请求，get调用
print(resp)
print(resp.text) # 拿到源代码