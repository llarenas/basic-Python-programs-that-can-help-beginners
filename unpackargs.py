'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''

def health(age, ate, smoke):
    answer=(100-age)+(ate*3.5) - (smoke *2)
    print(answer)

ronel = [23, 15, 9]
ronel1 = [24, 29, 29]

health(ronel[0], ronel[1], ronel[2],)
health(*ronel1)
    
