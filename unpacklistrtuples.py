'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''

date, item, price = ['december 23, 2015', 'bread', 8.34]
#print(item[2])
print(price)



##################################E###########################################

def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)

drop_first_last([65, 91, 63, 78, 88])
