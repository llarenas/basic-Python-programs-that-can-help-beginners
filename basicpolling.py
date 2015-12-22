'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''


TITLE = "Favourite Scripting Language?"
OPTION1 = "Python"
OPTION2 = "Java"
opt1 = 0
opt2 = 0


def main():
	user = input(TITLE + ", 1 = " + OPTION1 + ", 2 = " + OPTION2)
	while (user != '0'):
		try:
			u = int(user)
			if (u == 1):
			    opt1+=1
			elif (u == 2):
			    opt2+=1
			elif (u == 3):
			    print("Opt1: " + str(opt1) + ", Opt2: " + str(opt2))
		except:
			print("Failed")
			
		user = input(TITLE + ", 1 = " + OPTION1 + ", 2 = " + OPTION2)


main()
