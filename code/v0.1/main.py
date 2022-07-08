from random import randint
import sys
from hack import hack
from accounts import users


class Colours:
    YELLOW = '\33[93m'
    RED = '\33[91m'
    GREEN = '\33[92m'
    WHITE = '\33[0m'


TIMES_TRIED = 1

print("Welcome to Database Centre 1")
userInput = input("Enter Action: ")
print()
if userInput == "Enter Password":
    TRYING = True
    username = input(f"{Colours.WHITE}Enter Username: ")
    while TRYING:
        passwordInput = input(f"{Colours.WHITE}Enter Password: ")
        password = users.get(username)
        if passwordInput == password:
            print(f"{Colours.GREEN}Welcome {username}!")
            menuInput = input("Enter Action: ")
            if menuInput == "Change Password":
                NEW_PASSWORD = str(randint(0, 9999))
                users[username] = NEW_PASSWORD
                print(f"{Colours.GREEN}Password has been successfully changed.")
                sys.exit()
            elif menuInput == "Add New Account":
                if userInput.title() == "Admin Account":
                    newUsername = input("Enter New Username: ")
                    newPassword = int(input("Enter New Password: "))
                    users[newUsername] = newPassword
                    print(f"{Colours.GREEN}New user {newUsername} added!")
                else:
                    print(
                        f"{Colours.RED}You do not have permission to add a new account.")
        else:
            print(f"{Colours.RED}You got the wrong password.")
            if TIMES_TRIED == 3:
                print(f"{Colours.RED}You have used up all your tries.")
                TRYING = False
            else:
                TIMES_TRIED += 1
elif userInput == "Hack Password":
    hack()
