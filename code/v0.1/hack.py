def hack():
    from accounts import users
    hacked = False
    password_trying = 0000
    user_inquiry = input("Enter Username to Hack: ")
    password = users.get(user_inquiry)
    class Colours:
        YELLOW = '\33[93m'
        RED = '\33[91m'
        GREEN = '\33[92m'
        WHITE = '\33[0m'

    print(f"{Colours.YELLOW}Hacking...")
    while not hacked:
        if password_trying == password:
            print(
                f"{Colours.GREEN}Password cracked! The password is {password_trying}.")
            hacked = True
        else:
            print(f"{Colours.RED}Failed × ({password_trying}/9999)")
            password_trying += 1
