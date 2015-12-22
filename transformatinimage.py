'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''

from PIL import Image

baby = Image.open("baby.jpg")
s_baby = baby.resize((650, 250))
f_baby= baby.transpose(Image.FLIP_LEFT_RIGHT)

spin_baby = baby.transpose(Image.ROTATE_90)

baby.show()
s_baby.show()
f_baby.show()
spin_baby.show()
