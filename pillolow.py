'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''

from PIL import Image

img = Image.open("ronel.jpg") #convert image to pillw object
print(img.size)
print(img.format)

area = (50, 1, 950, 1575) #x & y, x & y. (kilid sa wala & babaw, kilid sa tuo & dalum)
cropped_img = img.crop(area)

#img.show()
cropped_img.show()
