#!/usr/bin/python3
#-*- coding:utf-8 -*-

import fofa
import math
import time
from bs4 import BeautifulSoup
from openpyxl import Workbook


def title():
	print('*-----------------------------------------*')
	print('!  \033[36mVersion: 1.0    \033[0m')
	print('!  \033[36m使用格式: python3 fofa_search.py    \033[0m')
	print('*-----------------------------------------*')

class FoFa:
	#初始化
	def __init__(self):
		self.mail="18850620382@139.com"
		self.key="645e0dd0bd7e0f0428c5f6183f32036d"
		try:
			self.api = fofa.Fofa(self.mail,self.key)
			#print('ok')
		except Exception as e:
			print('Error: {}'.format(e))

	def Search(self,dork):
		try:
			result = self.api.get_data(dork.encode())
			pages = math.ceil(result['size']/100)
			print('*-----------------------------------------*')
			print('!        \033[36m共{}页,{}条匹配结果\033[0m'.format(pages,str(result['size'])))
			print('*-----------------------------------------*')
			book = Workbook()
			sheet = book.active
			header=['IP','端口','URL','status','域名','服务','操作系统','国家','title','header']
			for h in range(len(header)):
				sheet.cell(row=1, column=h+1).value = header[h]
			k=2
			with open("Url.txt","a+") as fp:
				for i in range(1,min((math.ceil(result['size']/100)+1),101)):						
					print("正在保存第{}页数据".format(i))
					for ip,port,host,domain,server,os,country,title,header,isp in self.api.get_data(dork.encode(),i,fields="ip,port,host,domain,server,os,country,title,header,isp")['results']:
						try:					
							sheet.cell(row=k, column=1).value = str(ip)
						except Exception as e:
							print(e)
							pass
						try:					
							sheet.cell(row=k, column=2).value = str(port)
						except Exception as e:
							print(e)
							pass
						try:	
							if "https://" in host:				
								sheet.cell(row=k, column=3).value = str(host)
								fp.write(host+"\n")
							else:
								sheet.cell(row=k, column=3).value = str("http://"+host)
								fp.write("http://"+host+"\n")
						except Exception as e:
							print(e)
							pass
						try:
							status = int(header.split(' ')[1].strip())
							if status not in [200, 301, 302, 303, 304, 307, 400, 401, 403, 404, 405, 407,500, 501, 502, 503, 504, 508]:
								status = ''
						except:
							status = ''
						sheet.cell(row=k, column=4).value = status
						try:					
							sheet.cell(row=k, column=5).value = str(domain)
						except Exception as e:
							print(e)
							pass
						try:					
							sheet.cell(row=k, column=6).value = str(server)
						except Exception as e:
							print(e)
							pass					
						try:
							sheet.cell(row=k, column=7).value = str(os)
						except Exception as e:
							print(e)
							pass
						try:
							sheet.cell(row=k, column=8).value = str(country)
						except Exception as e:
							print(e)
							pass
						try:
							sheet.cell(row=k, column=9).value = str(title)
						except Exception as e:
							print(e)
							pass
						try:
							sheet.cell(row=k, column=10).value = str(header)
						except Exception as e:
							print(e)
							pass
						try:
							sheet.cell(row=k, column=11).value = str(isp)
						except Exception as e:
							print(e)
							pass
						k=k+1

						
				try:
					book.save("result.xlsx")
					print('查询结果已保存至当前目录下的result.xlsx!!!\n')
				except Exception as e:
					print('保存文件过程中出现异常，结果保存失败,！！！\n%s'%e)
			fp.close()
					
		except Exception as e:
			print('Error: {}'.format(e))
		

#def Search(dork):
    

if __name__ == '__main__':
	title()
	dork = str(input("\033[31m请输入Fofa查询语法:\nDork >>> \033[0m")) #定义字符颜色
	F=FoFa()
	F.Search(dork) 
