from random import randint
from hack import hack
import sys

class colours:
	YELLOW = '\33[93m'
	RED = '\33[91m'
	GREEN = '\33[92m'
	BLINK = '\33[6m'
	WHITE = '\33[0m'

times_tried = 1
trying = False

print("WELCOME TO Database Centre 1")
userInput = input("Enter Action: ")
print()
if userInput == "Enter Password":
	trying = True
	while trying:
		passwordInput = input(f"{colours.WHITE}Enter Password: ")
		file = open('password.txt', 'r')
		password = file.readline()
		if passwordInput == password:
			print(f"{colours.GREEN}{colours.BLINK}Welcome Ryan!")
			password = randint(0, 9999)
			file = open('password.txt', 'w')
			file.write(str(password))
			file.close()
			sys.exit()
		else:
			print(f"{colours.RED}You got the wrong password.")
			if times_tried == 3:
				print(f"{colours.RED}You have used up all your tries.")
				trying = False
			else:
				times_tried += 1
elif userInput == "Change Password":
	trying = True
	while trying:
		passwordInput = input(f"{colours.WHITE}Enter Password: ")
		file = open('password.txt', 'r')
		password = file.readline()
		if passwordInput == password:
			password = str(randint(0, 9999))
			file = open('password.txt', 'w')
			file.write(password)
			file.close()
			print(f"{colours.GREEN}Password has been successfully changed.")
			sys.exit()
		else:
			print(f"{colours.RED}You got the wrong password.")
			if times_tried == 3:
				print(f"{colours.RED}You have used up all your tries.")
				trying = False
			else:
				times_tried += 1
elif userInput == "Hack Password":
	hack()
