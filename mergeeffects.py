'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''


from PIL import Image
me1 = Image.open("ron.jpg")
me2 = Image.open("mename.jpg")
me3 = Image.open("222.jpg")

r2, g2, b2 = me1.split()
r1, g1, b1 = me2.split()
r3, g3, b3 = me3.split()

new_img = Image.merge("RGB", (r1,  g2, b3))
new_img.show()



##new_img = Image.merge("RGB", (b, r, g))
##new_img.show()
