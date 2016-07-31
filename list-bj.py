#encoding:UTF-8
#上海登陆信息
import datetime 
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  
import requests #__version__ = 2.3.0 这里直接使用session，因为要先登陆 
from bs4 import BeautifulSoup
#加了下面3行就不会有问题了（不知道是哪个编码的问题'btnquery'应该是gbk）

s = requests.session() #创建一个session对象
# x=循环金额范围 ， m=这个金额段的记录数 ，pg=总页数 ，n=
# link＝列表页url   r=列表页内容 ，link1=详情页url循环的页数
#北京先按照总价先选一遍
j=0
for x in range(5,1200,):
    for a in range(1,9,1):
        link="http://bj.lianjia.com/chengjiao/ddo21a" + str(a) + "bp" + str(x) + "ep" + str(x+1)
        r1 = s.get(link) #该页面进行登录，先获取一些信息
        bs=BeautifulSoup(r1.content).find("div",class_="total fl").find("span").get_text().strip()
        print link
        print time.ctime()
        pg=int(bs)/30+1
        print pg

        for n in range(1,int(pg)+1):
            link1="http://bj.lianjia.com/chengjiao/ddo21pg"+str(n)+ "a" + str(a) + "bp" + str(x) + "ep" + str(x+1)
            r2=s.get(link1)
            b1=BeautifulSoup(r2.content).find("ul",class_="listContent").find_all("li")
            
            print link1
            for i in b1:
                #print i
                #i=BeautifulSoup(markup)
                j=j+1
                print link1
                link2=i.find("a").get("href")
                print link2
                community=i.find("div",class_="title").get_text().strip().split(" ")[0]
                print community
                bedroom=i.find("div",class_="title").get_text().strip().split(" ")[1].split("室")[0]
                liveroom=i.find("div",class_="title").get_text().strip().split(" ")[1].split("室")[1].replace("厅","")
                space=i.find("div",class_="title").get_text().strip().split(" ")[2].split("平米")[0]
                orient=i.find("div",class_="address").find("div",class_="houseInfo").get_text().strip().split("|")[0]
                print orient,space,liveroom,bedroom
                dealtime=i.find("div",class_="address").find("div",class_="dealDate").get_text().strip()
                print dealtime
                totalprice=i.find("div",class_="address").find("div",class_="totalPrice").find("span").get_text().strip()
                print totalprice
                if str("(共") in i.find("div",class_="flood").find("div",class_="positionInfo").get_text().strip():
                    floor=i.find("div",class_="flood").find("div",class_="positionInfo").get_text().strip().split(" ")[0].split("(共")[0].replace("楼层","")
                    tfloor=i.find("div",class_="flood").find("div",class_="positionInfo").get_text().strip().split(" ")[0].split("(共")[1].replace("层)","")
                else:
                    floor=i.find("div",class_="flood").find("div",class_="positionInfo").get_text().strip().split(" ")[0]
                    tfloor="暂无信息"
                print floor
                print tfloor
                if len(i.find("div",class_="flood").find("div",class_="positionInfo").get_text().strip().split(" "))==2:
                    if str("年建") in i.find("div",class_="flood").find("div",class_="positionInfo").get_text():
                        if len(i.find("div",class_="flood").find("div",class_="positionInfo").get_text().strip().split(" ")[1].split("年建"))==2:
                            buildstyle=i.find("div",class_="flood").find("div",class_="positionInfo").get_text().strip().split(" ")[1].split("年建")[1]
                            completiontime=i.find("div",class_="flood").find("div",class_="positionInfo").get_text().strip().split(" ")[1].split("年建")[0]
                        else:
                            buildstyle=u"未知"
                            completiontime=i.find("div",class_="flood").find("div",class_="positionInfo").get_text().strip().split(" ")[1].split("年建")[0]

                    else:
                        buildstyle=i.find("div",class_="flood").find("div",class_="positionInfo").get_text().strip().split(" ")[1]
                        completiontime=u"未知"

                    

                else:
                    completiontime=u"未知"
                    buildstyle=u"未知"
                print completiontime
                
                unitprice=i.find("div",class_="flood").find("div",class_="unitPrice").get_text().strip().split("元/平")[0]
                #link2=i.find("a").get("href")
                #link2=i.find("div",class_='title').find("a").get("href")
                print buildstyle
                print unitprice
                print link2
                with open('list-bj.csv', 'a') as file:
                    file.write(str(j) +','+'北京' + ','+community+ ','+completiontime+','+bedroom+ ','+liveroom+ ','+orient+ ','+buildstyle+ ','+floor+ ','+tfloor+ ','+dealtime+ ','+space+ ','+totalprice+ ','+unitprice +','+link2+ '\n')
                file.close()
            if (j%25000==0):
                print time.ctime()
                print j

                time.sleep(2400)
                




                
            
'''            
            dealtime=BeautifulSoup(i.content).find("div",class_="wrapper").get_text("|", strip=True).split("|")[1].split(" ")[0]
            totalprice=BeautifulSoup(i.content).find("div",class_="price").find("span").find("i").get_text().strip()
                    unitprice=BeautifulSoup(i.content).find("div",class_="price").get_text("|",strip=True).split("|")[2]
                    housecode=BeautifulSoup(i.content).find("span",class_="house-code").get_text().replace("房源编号：","").strip()
                    bedroom=BeautifulSoup(i.content).find("span",class_="sp01").get_text("|", strip=True).split("|")[0].split("室")[0]
                    liveroom=BeautifulSoup(i.content).find("span",class_="sp01").get_text("|", strip=True).split("|")[0].split("室")[1].replace("厅","")
                    if str('(共') in BeautifulSoup(i.content).find("span",class_="sp01").get_text("|", strip=True).split("|")[1] :
                        floor=BeautifulSoup(i.content).find("span",class_="sp01").get_text("|", strip=True).split("|")[1].split("(共")[0].replace("楼层","")
                        tfloor=BeautifulSoup(i.content).find("span",class_="sp01").get_text("|", strip=True).split("|")[1].split("(共")[1].replace("层)","")
                    else:
                        floor=BeautifulSoup(i.content).find("span",class_="sp01").get_text("|", strip=True).split("|")[1]
                        tfloor="暂无信息"
                    orient=BeautifulSoup(i.content).find("span",class_="sp02").get_text("|", strip=True).split("|")[0]
                    #广州建成时间不在
                    #completiontime=BeautifulSoup(r1.content).find("span",class_="sp02").get_text("|", strip=True).split("|")[1]
                    completiontime=BeautifulSoup(i.content).find("span",class_="sp03").get_text("|", strip=True).split("|")[1].split("年建")[0] 

                    space=BeautifulSoup(i.content).find("span",class_="sp03").get_text("|", strip=True).split("|")[0].replace("平米","")
                    buildstyle=BeautifulSoup(i.content).find("span",class_="sp03").get_text("|", strip=True).split("|")[1].split("年建")[1]
                    community=BeautifulSoup(i.content).find("div",class_="info fr").find("p").get_text("|", strip=True).split("|")[0]
                    #中间有个“-”是[1]的值
                    district=BeautifulSoup(i.content).find("div",class_="info fr").find("p").get_text("|", strip=True).split("|")[2]
                    tradearea=
'''