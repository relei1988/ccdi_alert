#!/usr/bin/env python
# coding=utf-8
# code by cjj
# last modify time 2019.01.31
from bs4 import BeautifulSoup
import requests
import re
import json
import telegram
def chin(word):
	s = str(word).replace('u\'','\'')
	return s.decode("unicode-escape")


def write_data(list_link):
	with open("res.txt","w") as f:
		res = str(list_link)
		f.write(res)
		f.close()

def compare(content,list_link):
	with open('res.txt','r') as f:
		if content == f.read():
			f.close()
			return
			
		else:
			sendmessage(list_link)
			f.close()
			with open("res.txt","w") as f:
				f.write(content)
				f.close()
			
			
			
def sendmessage(list_link):
	with open('data.json','r') as f:
		data = eval(f.read())
		td = f.read()
		print len(td)
		f.close()


	for a in list_link:
		b = a.replace('href=".','http://www.ccdi.gov.cn/scdc')
		#print b
		addr = re.findall(r'(?<=<a ).*?(?=")',b)
		title = re.findall(r'(?<=blank">).*?(?=</a>)',b)
		date = re.findall(r'(?<=<span>).*?(?=</span>)',b)
		if title[0] not in data:
			data[title[0]] = {"date":date[0],"addr":addr[0]}
			b = date[0]+" " + title[0] + " " + addr[0]
			print b
			#bot.send_message("@channelname", b)



		#bot.send_message("@channelname", b)	
	#print chin(data)
	#data为获取当前最新公告，转化为dict，{'吉林白城市人大常委会原党组书记王锐接受审查调查': {'date': '2019-02-01', 'addr': 'http://www.ccdi.gov.cn/scdc/sggb/zjsc/201902/t20190201_188187.html'}, '哈尔滨金融学院原党委书记邓福庆接受监察调查': {'date': '2019-01-28', 'addr': 'http://www.ccdi.gov.cn/scdc/sggb/zjsc/201901/t20190128_187829.html'}}
	with open("data.json","w") as f:
		f.write(str(data))
		f.close()





#bot = telegram.Bot(token='YOURTOKEN')

r = requests.get("http://www.ccdi.gov.cn/scdc/")
r.encoding='utf-8'
res = r.text
soup = BeautifulSoup(res, "lxml")
link = chin(soup.find_all("ul",{'class':'list_news_dl fixed'}))
#print link
link = link.replace("\n","")
list_link = re.findall(r'(?<=<li>).*?(?=</li>)',link)
stl = str(list_link)
compare(stl,list_link)


#print chin(list_link)



# #print link,type(link)
# print list_link
