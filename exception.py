'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''

##una = int(input("wahats ur numbah? \n"))
##print(una)


while True:
    try:
        number = int(input("whats ur fav numbah? \n"))
        print(18/number)
        break
    except ValueError:
        print("make sure u enter number!! ")
    except ZeroDivisionError:
        print("wag zero!! ")
    except:
        break
    finally:
        print("execute n matter what!")
