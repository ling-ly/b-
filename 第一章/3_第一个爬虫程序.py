# 作者：ling-ly
# 开发时间：2023/2/18 9:33
# 爬虫：通过编写程序来获取到互联网上的资源
# b站？百度
# 需求：用程序模拟浏览器，输入一个网址，从该网站中获取到资源或者内容
# python搞定以上需求，特别简单

from urllib.request import urlopen
# 从urllib库中引入urlopen,即请求打开链接
url = "http://www.baidu.com/"
resp = urlopen(url)     # 打开百度并将网页源代码赋予resp

# print(resp.read().decode("utf-8"))
# # resp.read()得到的是二进制代码，所有要使用decode方法进行解码
with open("mybaidu.html","w",encoding="utf-8") as f:    # 创建文件
    f.write((resp.read().decode("utf-8")))    # 保存写入  # 读取网页源代码
# 如果发现读的文件很小是window打开文件默认是以“gbk“编码的，可能造成不识别unicode字符
# 解决办法"mybaidu.html","w",???encoding="utf-8"???  即？？？这句话？？？
print("over")