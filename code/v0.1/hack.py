def hack():
	hacked = False
	password_trying = 0000
	file = open('password.txt', 'r')
	password = int(file.readline())
	
	class colours:
		YELLOW = '\33[93m'
		RED = '\33[91m'
		GREEN = '\33[92m'
	
	print(f"{colours.YELLOW}Hacking...")
	while not hacked:
		if password_trying == password:
			print(f"{colours.GREEN}Password cracked! The password is {password}.")
			hacked = True
		else:
			print(f"{colours.RED}Failed × ({password_trying}/9999)")
			password_trying += 1
			file = open('password_trying', 'w')
			file.write(str(password_trying))
			file.close()
