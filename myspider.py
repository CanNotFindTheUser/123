# import requests
# from bs4 import BeautifulSoup
# import time
#
# def get_url(word):
# 	return 'http://dict.youdao.com/w/eng/'+word+'/#keyfrom=dict2.index'
#
#
# def zhaoYinBiao(url):
# 	import requests
# 	from bs4 import BeautifulSoup
#
# 	user_agent = 'Mozilla/4.0 (compatible;MSIE 5.5;Windows NT)'
# 	headers = {'User-Agent': user_agent}
#
# 	html = requests.get(url, headers=headers).text
# 	soup = BeautifulSoup(html, 'lxml')  # 传入html源代码字符串，BeautifulSoup对象
#
# 	return soup.find(class_='phonetic').string   # 获得文本内容
#
#
#
#
# if __name__ == '__main__':
# 	import re
# 	pattern = re.compile(r'[A-Za-z]+')
#
# 	f1 = open('4000-4299.txt', 'r')
# 	f2 = open('4000-4299(1).txt', 'a', encoding='utf-8')
#
# 	for number_word in f1.readlines():
# 		word = re.search(pattern, number_word).group()
# 		try:
# 			yinBiao = zhaoYinBiao(word)
# 		except AttributeError:
# 			yinBiao ='%%%'
# 		f2.write(number_word.strip('\n')+' '*(20-len(number_word))+yinBiao+'\n')  # .strip('\n')
# 		print(word)
#
# 	f1.close()
# 	f2.close()
#
import requests
from bs4 import BeautifulSoup
import time


def get_url(word):
	return 'http://dict.youdao.com/w/eng/' + word + '/#keyfrom=dict2.index'


def find_yin_biao(new_urls):
	import requests
	from bs4 import BeautifulSoup

	user_agent = 'Mozilla/4.0 (compatible;MSIE 5.5;Windows NT)'
	headers = {'User-Agent': user_agent}

	if len(new_urls) != 0:
		url = new_urls.pop()
		try:
			html = requests.get(url, headers=headers).text
			soup = BeautifulSoup(html, 'lxml')  # 传入html源代码字符串，BeautifulSoup对象
			return soup.find(class_='phonetic').string  # 获得文本内容
		except AttributeError:
			return '%%%'


if __name__ == '__main__':
	import re

	pattern = re.compile(r'[A-Za-z]+')

	f1 = open('4300-4499.txt', 'r')
	f2 = open('4300-4499(1).txt', 'a', encoding='utf-8')  # 写入文件encoding='utf-8'

	new_urls = []
	old_urls = []  # 没用...
	for number_word in f1.readlines():
		word = re.search(pattern, number_word).group()
		new_urls.append(get_url(word))

		while len(new_urls) != 0:
			yin_biao = find_yin_biao(new_urls)

			f2.write(number_word.strip('\n') + ' ' * (20 - len(number_word)) + yin_biao + '\n')  # .strip('\n')
			print(word, '---------还有', len(new_urls), '个')  # 这里的缩进不对，但不好改

	f1.close()
	f2.close()

