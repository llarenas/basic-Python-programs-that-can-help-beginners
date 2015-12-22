'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''


from PIL import Image

si = Image.open("si.jpg")
yvonne = Image.open("1.jpg")

area = (400, 300)

si.paste(yvonne, area)

si.show()
