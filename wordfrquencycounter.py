'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''

import requests
from bs4 import BeautifulSoup
import operator


def start(url):
    word_list = []
    surce_code = requeasts.get(url).text
    soup = BeautifulSoup(source_code)
    for post_text in soup.findAll('a', {'class':'dx'}):
        content = post_text.string
        words = content.lower().split()
        for each_word in words:
           # print(each_word)
            word_list.append(each_word)
        clean_up_list(word_list)

def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "!@#$%^&*(,):.?\":';<>\|~`"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")

        if len(word) > 0:
            print(word)
            clean_word_list.append(word)

    create_dictionary(clean_word_list)


def create_dictionary(clean_word_list):
    word_count={}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] +=1
        else:
            word_count[word] =1
            
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)): #1 kung value, 0 kung key.
        print(key, value)


            


start('https://free.facebook.com/home.php?ref_component=mbasic_home_logo&ref_page=%2Fwap%2Fphoto.php&refid=13')
