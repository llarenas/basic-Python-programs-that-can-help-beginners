'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''

import random
import urllib.request

def download_web_image(url):
    print('Downloading')
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)
    print('photo Downloaded')


download_web_image("https://scontent-dfw1-1.xx.fbcdn.net/hphotos-xtf1/t31.0-8/1412249_10153876254109047_4858625670534020761_o.jpg?efg=eyJpIjoibyJ9")

    

    
