'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''

class Enemy :
    life = 3

    def attack(self):
        print('ouch!')
        self.life -=1


    def chcklife(self):
        if self.life <=0:
            print('I am dead')

        else:
            print(str(self.life) + " life left" )

