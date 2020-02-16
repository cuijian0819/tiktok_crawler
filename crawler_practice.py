import requests
import re

# target url
url = 'https://www.17k.com/list/3073808.html'

# get response html content
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

dl = re.findall(r'<dl class="Volume">(.*?)</dl>', html, re.S)[1]

dd = re.findall(r'<dd>(.*?)</dd>', html, re.S)[1]

aill = re.findall(r'href="(.*?)">(.*?)<', dd, re.S)

# get title from html
title = re.findall(r'<h1 class="Title">(.*?)</h1>',html, re.S)[0]

f = open(f"{title}.txt",'w',encoding="utf-8")

for i in range(10):
	# extract url and title
	chapter_url = 'https://www.17k.com' + aill[i][0].split('"')[0]
	chapter_title = aill[i][0].split('"')[2].split('&')[0]

	# get chapter response html content
	response = requests.get(chapter_url)
	response.encoding = 'utf-8'
	chatper_html = response.text

	# find chapter content and edit 
	chapter_content = re.findall(r'<div class="p">(.*?)</div>', chatper_html, re.S)[0]
	chapter_content = chapter_content.replace(' ', '')
	chapter_content = chapter_content.replace('<p>', '')
	chapter_content = chapter_content.replace('</p>', '')

	# write to the new file 
	f.write(f"{chapter_title}\n")
	f.write(f"{chapter_content}\n")
	f.write("\n")


