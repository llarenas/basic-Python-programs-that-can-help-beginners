'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''

class Parent():
    def print_last_name(self):
        print('bugarin')

class Child(Parent):

    def print_first_name(self):
        print('nel')

    def print_last_name(self): #override ang lastname sa parent class.
        print('llarenas')

ron = Child()
ron.print_first_name()
ron.print_last_name()
    
