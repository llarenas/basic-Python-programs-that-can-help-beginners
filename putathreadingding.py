'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''

import threading

class Mymessenger(threading.Thread):

    def run(self): # kailan sang amo ni nga functin every thread, pwede man isulod ang init functin dri.
        for _ in range(10): #kung ayaw mglagay m ng letter var. pwede _ lng ilagay
            print(threading.currentThread().getName()) #threading code para mag thread r mag run ang thread class..

x = Mymessenger(name='send ur messages \n')
y = Mymessenger(name='receive')
x.start() #basta thread, start ibutang imbes na ang classname.
y.start()
