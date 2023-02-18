# 作者：ling-ly
# 开发时间：2023/2/18 15:45
import requests
url = "https://fanyi.baidu.com/sug"
words = input("请输入你要翻译的英语单词\n")
datas = {
    "kw":words  # 在负载中找到kw
}

resp = requests.post(url,data=datas)    ##get请求数据是params
# resp = requests.post(url,dates) 同上面的效果
# print(resp.text)会有乱码
# {"errno":0,"data":[{"k":"for","v":"prep. \u4e3a\uff0c\u4e3a\u4e86;
print(resp.json())  # python字典
# [{'k': 'keep', 'v': 'vt. 保持; 保留; 遵守; 阻止 vi. （食品）保持新; 保持健康 n. 保持，保养; 供养，'},]
