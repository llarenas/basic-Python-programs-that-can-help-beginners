'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''


class Mario():
    def move(self):
        print('i am moving ! ')

class Shroom():
    def eats(self):
        print('nw i am big! ')



#bisan wala unod k lang, butngan mo lang pass. kay nag inherit mn sya sa nauna nga duwa nga class.
class Bigmario(Mario, Shroom):

    pass

bm =Bigmario()
bm.move()
bm.eats()

    
