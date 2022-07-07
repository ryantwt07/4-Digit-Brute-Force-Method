def hack():
	hacked = False
	password_trying = 0000
	userInquiry = input("Enter Username to Hack: ")
	file = open('accounts.txt', 'r')
	account_dict = file.readlines()
	password = account_dict.get(userInquiry)
	
	class colours:
		YELLOW = '\33[93m'
		RED = '\33[91m'
		GREEN = '\33[92m'
		WHITE = '\33[0m'
	
	print(f"{colours.YELLOW}Hacking...")
	while not hacked:
		if password_trying == password:
			print(f"{colours.GREEN}Password cracked! The password is {password_trying}.")
			hacked = True
		else:
			print(f"{colours.RED}Failed × ({password_trying}/9999)")
			password_trying += 1