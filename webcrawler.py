'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''

import requests
from bs4 import BeautifulSoup   #idownlad pa needed ang module nga beautifulsoup.

def trade_spider(max_pages):
    page = 1

    while page <= max_pages:
        url = 'http://www.redtube.com/?search=milf' + str(page)
        sourcecode=requests.get(url)
        plain_text = sourcecode.text
        #soup = BeautifulSoup(plain_text)
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll('a', {'class': 'item-name'}): # a as <a href> </a>, item-name is name sang class sng link.
            href = "https://redtube.com" + link.get('href')
            title = link.string # get the text in the link.
            #print(href)
            #print(title)
            get_single_item_data(item_url)
        page+= 1

def get_single_item_data(item_url):
    sourcecode=requests.get(item_url)
    plain_text = surcecode.text
    #soup = BeautifulSoup(plain_text)
    soup = BeautifulSoup(plain_text, "html.parser")
    for item_name in soup.findAll('div', {'class': 'i-name'}):
        print(item_name.string)
    for link in soup.findAll('a'):
         href = "https://redtube.com" + link.get('href')
         print(href)
    

        

trade_spider(3)
            
        
    


