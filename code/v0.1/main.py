from random import randint
from hack import hack
import sys

class colours:
	YELLOW = '\33[93m'
	RED = '\33[91m'
	GREEN = '\33[92m'
	WHITE = '\33[0m'

times_tried = 1
trying = False

print("Welcome to Database Centre 1")
userInput = input("Enter Action: ")
print()
if userInput == "Enter Password":
	trying = True
	userInput = input(f"{colours.WHITE}Enter Username: ")
	while trying:
		passwordInput = input(f"{colours.WHITE}Enter Password: ")
		accounts_file = open('accounts.txt', 'r')
		accounts_dict = accounts_file.readlines()
		password = accounts_dict.get(userInput.title())
		if passwordInput == password:
			print(f"{colours.GREEN}{colours.BLINK}Welcome Ryan!")
			password = randint(0, 9999)
			file = open('password.txt', 'w')
			file.write(str(password))
			file.close()
			menuInput = input("Enter Action: ")
			if menuInput == "Change Password":
				new_password = str(randint(0, 9999))
				file = open('password.txt', 'w')
				file.write(password)
				file.close()
				print(f"{colours.GREEN}Password has been successfully changed.")
				sys.exit()
			elif menuInput == "Add New Account":
				if userInput.title() == "Admin Account":
					newUsername = input("Enter New Username: ")
					newPassword = int(input("Enter New Password: "))
					accounts_dict[newUsername] = newPassword
					print(f"{colours.GREEN}New user {newUsername.title} added!")
				else:
					print(f"{colours.RED}You do not have permission to add a new account. Please use the admin account.")
		else:
			print(f"{colours.RED}You got the wrong password.")
			if times_tried == 3:
				print(f"{colours.RED}You have used up all your tries.")
				trying = False
			else:
				times_tried += 1
elif userInput == "Hack Password":
	hack()
