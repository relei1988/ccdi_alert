#!/usr/bin/env python
# coding=utf-8
# code by cjj
# last modify time 2019.01.31
from bs4 import BeautifulSoup
import requests
import re
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
			return
			f.close()
		else:
			sendmessage(list_link)
			f.close()
			with open("res.txt","w") as f:
				f.write(content)
				f.close()
			
			
			
def sendmessage(list_link):
	for a in list_link:
		b = a.replace('href=".','http://www.ccdi.gov.cn/scdc')
		bot.send_message("@channelname", b)




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
