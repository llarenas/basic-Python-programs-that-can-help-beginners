'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''

from PIL import Image
from PIL import ImageFilter

baby = Image.open("ron.jpg")

black_white = baby.convert("L")
blur = baby.filter(ImageFilter.BLUR)
detail = baby.filter(ImageFilter.DETAIL)
edges = baby.filter(ImageFilter.FIND_EDGES)


black_white.show()

blur.show()
detail.show()
edges.show()



