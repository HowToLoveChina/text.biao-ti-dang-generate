from 辅助函数 import *

文章长度 = 2000

数据 = 读JSON文件("数据")
姓数据库 = 数据["姓"]
名数据库  = 数据["名"]
前置标题数据库 = 数据["前置标题数据库"]
后置标题数据库 = 数据["后置标题数据库"]
正文废话 = 数据["正文废话"]
狗屁结论 = 数据["狗屁结论"]

模板 = ""
with open("网页模板.html","r",encoding="utf-8") as 文件:
    模板 = 文件.read()

大废话 = input("请输入一句废话:")

标题 = 生成标题(大废话,前置标题数据库,后置标题数据库)

配一张图 = 爬取图片(大废话)
专家名称 = 生成人名(姓数据库,名数据库,人名长度=随便来一个数(最小值 = 2,最大值 = 3))
废话生成器 = 来点废话(大废话,正文废话,专家名称)
临时文本 = ""
while(len(临时文本) < 文章长度):
    随机数 = 随便来一个数(最小值 = 0,最大值 = 100)
    if 随机数<5:
        临时文本 += 另起一段()
    elif 随机数 <10:
        临时文本 += next(配一张图)
    else:
        临时文本 += next(废话生成器)

临时文本 += 加上结论(大废话,狗屁结论)

文章全部内容 = 模板.replace("【标题】",标题).replace("【正文】",临时文本)

with open(os.path.join("文章",标题+".html"),"w",encoding="utf-8") as 文件:
    文件.write(文章全部内容)
print("标题党网页“"+标题+"”已生成在“文章”文件夹下")