#encoding:utf-8
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
'''
#post的消息
From_Data = {
    'username':'18515907187',
    'password':'ljjory',
    'execution':'e1s1',
    '_eventId':'submit',
    'remember':'1',
    'redirect':'',
    'verifyCode':'',
    'lt':'LT-2050351-VAQhRU47VNOsq5MqcdGjJFhwrofQ9Y-www.lianjia.com'
}
Cookies = {
    'JSESSIONID':'97E8CBCFAB21C91DBFF496B9649D9985-n1',
    'lianjia_uuid':'de01012f-8e3f-4e51-9c26-074e908ec389',
    '_ga':'GA1.2.1780588919.1453172278',
    '_jzqa':'1.93982205891852130.1453172279.1453174656.1454399936.3',
    'select_city':'310000',
    'cityCode':'sh',
    'ubt_load_interval_b':'1469443418330',
    'ubt_load_interval_c':'1469443418330',
    'ubta':'2299869246.864786360.1469443176292.1469443420395.1469443421755.7',
    'ubtb':'2299869246.864786360.1469443421759.9D5A5C84C523FFAEFB8B8A9A4840DE02',
    'ubtc':'2299869246.864786360.1469443421759.9D5A5C84C523FFAEFB8B8A9A4840DE02',
    'ubtd':'7',
    'lianjia_ssid':'b74dc073-e876-4729-82eb-f9fe4e82475f',
    'gr_user_id':'99b4710a-1bea-4c76-842a-e33df3e420df',
    'gr_session_id_970bc0baee7301fa':'bc36c4e4-483f-4e55-850e-286e8f54f7e1',
    '_gat':'1',
    'gr_cs1_bc36c4e4-483f-4e55-850e-286e8f54f7e1':'userid%3A2000000008495819',
    'pt_s_393d1d99':'vt=1469443419636&cad=',
    'pt_393d1d99':'uid=54WLHuNdh9e1AXXwPfiRaQ&nid=0&vid=zaZN9/D8xtU8rFxuB0t/Nw&vn=1&pvn=7&sact=1469443421799&to_flag=0&pl=Rxfrwx1FynKx2dVA3ilg4w*pt*1469443419636'
}


header = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    #'Accept-Encoding':'gzip, deflate',
    #'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
    'Connection':'keep-alive',
    #'Cookie':Cookies,
    'Host':'passport.lianjia.com',
    'Referer':'https://passport.lianjia.com/cas/login?service=http://user.sh.lianjia.com/index/ershou',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:35.0) Gecko/20100101 Firefox/35.0',
    'Content-Length':'161',
    'Content-Type':'application/x-www-form-urlencoded'
}
url='https://api.growingio.com/v2/970bc0baee7301fa/web/action?stm=1469501667781'
response3=s.get(url)
response1=s.post(url,data=From_Data,headers=header)
bs1=BeautifulSoup(response1.content)
'''

'''
#看全部房源总数
response2=s.get('http://sh.lianjia.com/chengjiao')
bs2=BeautifulSoup(response2.content).find("h2",attrs={"style":"float:left"}).find("span").get_text().strip()
print bs2

'''

#还是登陆不进去，


j=0

#每1平米间隔一次,先统计2到200
for x in range(5,200,1):
    link="http://sh.lianjia.com/chengjiao/m" + str(x) + "to" + str(x+1)
    #print link
    r = s.get(link) #该页面进行登录，先获取一些信息
    bs = BeautifulSoup(r.content).find("h2",attrs={"style":"float:left"}).find("span").get_text().strip()
    pg=int(bs)/20+1
    print bs
    print link

    for n in range(1,int(pg)+1):
        link1="http://sh.lianjia.com/chengjiao/d"+str(n)+"m"+str(x)+"to"+str(x+1)
        print link1
        b1=s.get(link1)
        bs1=BeautifulSoup(b1.content).find("ul",class_="clinch-list").find_all("li")
        print len(bs1)
        for b2 in bs1:
            j=j+1
            
            community=b2.find("h2",class_="clear").find("a").get_text().strip().split(" ")[0]
            bedroom=b2.find("h2",class_="clear").find("a").get_text().strip().split(" ")[1].split("室")[0]
            liveroom=b2.find("h2",class_="clear").find("a").get_text().strip().split(" ")[1].split("室")[1].replace("厅","")
            space=b2.find("h2",class_="clear").find("a").get_text().strip().split(" ")[2].replace("平米","")
            district=b2.find("div",class_="con").find_all("a")[0].get_text().strip()
            tradearea=b2.find("div",class_="con").find_all("a")[1].get_text().strip()
            txt=b2.find("div",class_="con").get_text("",strip=True)
            #print txt
            if txt.count("|")==3:
                orient=txt.split("|")[2]
            if txt.count("|")==2:
                if str("朝") in txt:
                    orient=txt.split("|")[2]
                else:
                    orient=u"暂无信息"
            if txt.count("|")==1:
                orient=u"暂无信息"
            if txt.split("|")[1].count("/") ==1:
                floor=txt.split("|")[1].split("/")[0].replace("层","")
                tfloor=txt.split("|")[1].split("/")[1].replace("层","")
            else:
                floor=txt.split("|")[1]
                tfloor=u"暂无信息"
            txt2=b2.find("div",class_="dealType").get_text("|",strip=True)
            #print txt2
            dealtime=txt2.split("|")[0]
            unitprice=txt2.split("|")[2]
            totalprice=txt2.split("|")[5]
            link0=str("http://sh.lianjia.com/")+b2.find("h2",class_="clear").find("a")["href"]
            print link1
            print link0
            print dealtime
            print totalprice
            print unitprice
            #print housecode
            print bedroom
            print liveroom
            print floor
            print tfloor
            print orient
            #print completiontime
            print space
            print community
            print district
            print tradearea

            with open('shanghailianjia.csv', 'a') as file:
                file.write(str(j) +','+'上海' + ','+district+ ','+tradearea+ ','+community+ ','+bedroom+ ','+liveroom+ ','+orient+ ','+floor+ ','+tfloor+ ','+dealtime+ ','+space+ ','+totalprice+ ','+unitprice +','+link0+ '\n')
            file.close()
            if (j%30000==0):
                print time.ctime()
                print j
                time.sleep(2400)
            














'''
                print dealtime
                print totalprice
                print unitprice
                print housecode
                print bedroom
                print liveroom
                print floor
                print tfloor
                print orient
                print completiontime
                print space
                print community
                print district
'''

'''
        for link0 in bs1:
            if link0.find('a') is None:
                continue
            else:
                link0='http://sh.lianjia.com/'+link0.find('a').get('href')
                #print link0
                b2=s.get(link0)
                j=j+1
                dealtime=BeautifulSoup(b2.content).find('div',class_='cell first').find('p').get_text().strip()
                #【这样写貌似识别第一个是cell的】totalprice=BeautifulSoup(b2.content).find('div',attrs={'class':'cell'}).find('p').get_text("|",strip=True)#.split("|")[0]
                totalprice=BeautifulSoup(b2.content).find('span',class_='unit').parent.get_text("|",strip=True).split("|")[0]
                unitprice=BeautifulSoup(b2.content).find('td',attrs={'colspan':'2'}).get_text("|",strip=True).split("|")[1].replace("元/平","")
                housecode=BeautifulSoup(b2.content).find(text="房源编号：").parent.parent.get_text("|", strip=True).split("|")[1]
                bedroom=BeautifulSoup(b2.content).find('div',class_='title-box').find("h1").get_text().split(" ")[1].split("室")[0]
                liveroom=BeautifulSoup(b2.content).find('div',class_='title-box').find("h1").get_text().split(" ")[1].split("室")[1].split("厅")[0]
                floor=BeautifulSoup(b2.content).find(text="楼层：").parent.parent.get_text("|",strip=True).split("|")[1].split("/")[0]
                print floor,link0

                tfloor=BeautifulSoup(b2.content).find(text="楼层：").parent.parent.get_text("|",strip=True).split("|")[1].split("/")[1]
                orient=BeautifulSoup(b2.content).find(text="朝向：").parent.parent.get_text("",strip=True).replace("朝向：","")#.split("|")[1]
                
                if orient == "": #orient[-1]=='|':
                    orient=str('暂无信息')
                completiontime=BeautifulSoup(b2.content).find(text="年代：").parent.parent.get_text("|",strip=True).split("|")[1].split("年建")[0]
                space=BeautifulSoup(b2.content).find('div',class_='title-box').find("h1").get_text().split(" ")[2].split("平米")[0]
                community=BeautifulSoup(b2.content).find(text="小区：").parent.parent.find("a").get_text().strip()
                district=BeautifulSoup(b2.content).find(text="小区：").parent.parent.get_text("|",strip=True).split("|")[2].replace("（","").replace("）","").split(" ")[0]
                tradearea=BeautifulSoup(b2.content).find(text="小区：").parent.parent.get_text("|",strip=True).split("|")[2].replace("（","").replace("）","").split(" ")[1]
                with open('shanghailianjia.csv', 'a') as file:
                    file.write(str(j) +','+'上海' + ','+district+ ','+tradearea+ ','+community+ ','+completiontime+','+housecode+ ','+bedroom+ ','+liveroom+ ','+orient+ ','+floor+ ','+tfloor+ ','+dealtime+ ','+space+ ','+totalprice+ ','+unitprice +','+link0+ '\n')
                file.close()
                if (j%1200==0):
                    print time.ctime()
                    print j
                    time.sleep(2400)
'''
