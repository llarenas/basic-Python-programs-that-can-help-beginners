'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''


def add(*taeargs): #*taeargs means all number per line, * means accepting multiple value per line
    total = 0
    for a in taeargs: # a is variable meaning each. each multiple value per line
        total +=a       #total is variable in adding all multiple value in each line
    print(total)


add(3)
add(3, 45)
add(6, 7, 778, 8755, 99, 12578)
    
