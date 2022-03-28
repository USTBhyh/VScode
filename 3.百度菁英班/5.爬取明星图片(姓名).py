# 首先我们要导入相关的包
# request：提供爬虫相关的接口函数
# json：主要负责处理字典类型数据在字符串与字典之间进行转换
import requests
import json
import os


# 直接使用程序爬取网络数据会被网站识别出来，然后封禁该IP，导致数据爬
# 取中断，所以我们需要首先将程序访问页面伪装成浏览器访问页面
# User-Agent：定义一个真实浏览器的代理名称，表明自己的身份（是哪种浏览器），本demo为谷歌浏览器
# Accept：告诉WEB服务器自己接受什么介质类型，*/* 表示任何类型
# Referer：浏览器向WEB服务器表明自己是从哪个网页URL获得点击当前请求中的网址/URL
# Connection：表示是否需要持久连接
# Accept-Language：浏览器申明自己接收的语言
# Accept-Encoding：浏览器申明自己接收的编码方法，通常指定压缩方法，是
# 否支持压缩，支持什么压缩方法（gzip，deflate）
def getPicinfo(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        "Accept": "*/*",
        "Referer": "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E4%B8%AD%E5%9B%BD%E8%89%BA%E4%BA%BA&fenlei=256&rsv_pq=cf6f24c500067b9f&rsv_t=c2e724FZlGF9fJYeo9ZV1I0edbhV0Z04aYY%2Fn6U7qaUoH%2B0WbUiKdOr8JO4&rqlang=cn&rsv_dl=ib&rsv_enter=1&rsv_sug3=15&rsv_sug1=6&rsv_sug7=101",
        "Host": "sp0.baidu.com",
        "Connection": "keep-alive",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6",
        "Accept-Encoding": "gzip, deflate"
    }
    # 根据url，使用get()方法获取页面内容，返回相应
    response = requests.get(url,headers)  
    # 成功访问了页面
    if response.status_code == 200:
        return response.text
    # 没有成功访问页面，返回None
    return None

#图片存放地址
Download_dir='picture'
if os.path.exists(Download_dir)==False:
    os.mkdir(Download_dir)

pn_num=1  #  爬取多少页
rn_num=10  #  每页多少个图片

for k in range(pn_num):  # for循环，每次爬取一页
	url="https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=28266&from_mid=1&&format=json&ie=utf-8&oe=utf-8&query=%E4%B8%AD%E5%9B%BD%E8%89%BA%E4%BA%BA&sort_key=&sort_type=1&stat0=&stat1=&stat2=&stat3=&pn="+str(k)+"&rn="+str(rn_num)+"&_=1613785351574"
	
	res = getPicinfo(url)       # 调用函数，获取每一页内容
	json_str=json.loads(res)    # 将获取的文本格式转化为字典格式
	figs=json_str['data'][0]['result']  
	
	for i in figs:              # for循环读取每一张图片的名字
		name=i['ename']
		img_url=i['pic_4n_78']  # img_url：图片地址
		img_res=requests.get(img_url)  # 读取图片所在页面内容
		if img_res.status_code==200: 
			ext_str_splits=img_res.headers['Content-Type'].split('/')
			ext=ext_str_splits[-1]  # 索引-1指向列表倒数第一个元素
			fname=name+"."+ext
            # 保存图片
			open(os.path.join(Download_dir,fname),  'wb' ).write(img_res.content)
			print(name,img_url,"saved")
