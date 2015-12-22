'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''


class Girl:
    gender = 'female'     # class variable= default every object



    def __init__(self, name):  # class instance variable = unique.
        self.name = name
        


r = Girl (input('enter girl name: '))
s = Girl (input('name pa gd: '))


#nami ni nga frmat kay ako naghimo

print(r.gender, r.name)
print(s.gender, s.name)


#amo ni previus.
##print(r.gender)
##print(s.gender)
##
##print(r.name)
##print(s.name)
