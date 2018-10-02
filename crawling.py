#!/usr/bin/python3

import re
import requests
import os
import sys
import time
import platform

crawl = []
crawled = set()
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
			                        'AppleWebKit/537.36 (KHTML, like Gecko)'
			                        'Chrome/51.0.2704.103 Safari/537.36'}

class bcolors:
	red = ('\033[91m')
	endc= ('\033[0m')

def help():
	so = platform.system()
	if so == 'Windows':
		os.system('cls')
	else:
		os.system('clear')
	
	banner = """
		 ||  ||  
 		 \\\()//                WEB CRAWLING
		//(__)\\    "My name is Linus, and I am your God."
	        ||    ||     
	                  Use: python3 crawling.py --notice [LINUS-IS-A-GOD?]	                                                   
		 	  Use: python3 crawling.py --url [https://www.microsoft.com]		 	                                         
		"""
	print(banner)



banner =   """
			Remember manual search, best that automated search
			Use and abuse! @ github.com/fyoderxx -------------
			"Talking is easy, show me the code."
			"""
print(banner)


def connect():	
	if len(sys.argv) < 3:
		print(help())
	elif sys.argv[1] == "--notice":
		notice = sys.argv[2]
		notc = ('https://www.google.com.br/search?q='+notice)
		crawl.append(notc)
	elif sys.argv[1] == "--url":
		site = sys.argv[2]
		sitedu = (site)
		crawl.append(sitedu)

def main():
	try:
		connect()
		while True:
				url = crawl[0]
				try:
					req = requests.get(url, headers=header)
				except:
					crawl.remove(url)
					crawled.add(url)
				
				html = req.text
				exp = re.findall(r'<a href="?\'?(https?:\/\/[^"\'>]*)', html)
				time.sleep(1)
				print(bcolors.red + '[*] Crawling: ' + bcolors.endc, url)
				crawl.remove(url)
				crawled.add(url)
				for link in exp:	
					if link not in crawled and link not in crawl:
						crawl.append(link)	
	except Exception as e: 
		print(help())
		

if __name__ == "__main__":
	try:
		main()
	except(KeyboardInterrupt):
		print('\nBye...')
		exit(0)
