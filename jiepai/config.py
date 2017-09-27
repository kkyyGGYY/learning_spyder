"""
- 1、抓取索引页内容：
利用requests请求目标站点，得到索引网页html代码，返回结果

- 2、抓取详情页内容：
解析返回结果，得到详情页的链接，并进一步抓取详情页的信息

- 3、下载图片与保存数据库：
将图片下载到本地，并把页面信息及图片urlbao保存至MongoDB。

- 4、开启循环及多线程：
对多页面内容遍历，开启多线程提高抓取速度
"""

MONGO_URL = 'localhost'
MONGO_DB = 'toutiao'
MONGO_TABLE = 'toutiao'


GROUP_START = 1
GROUP_END = 20

KEYWORD = '街拍'