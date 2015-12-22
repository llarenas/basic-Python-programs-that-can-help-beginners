'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''


from PIL import Image

gft = Image.open("gft.jpg")

#print(gft.mode)
r, g, b =gft.split()

r.show()
g.show()
b.show()
