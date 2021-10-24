import webbrowser 
from bs4 import BeautifulSoup
import requests


def perform_search():
	term = input("What would you like to search for: ")
	pre = "https://www.google.com/search?q="
	url = pre + term
#	webbrowser.open_new(pre)
	page = requests.get(url)#, headers=headers)
	soup = BeautifulSoup(page.content, 'html.parser')
	t = soup.find("h3").parent
	tag = str(t)
	splitTag = tag.split()
	lst = []
	for i in splitTag:
		if i.startswith("href"):
			x = i.split('"')
			lst.append(x[1])
	link = lst[0]
	l = link[7:]
	print(l)
	webbrowser.open_new(l)
	exit()
