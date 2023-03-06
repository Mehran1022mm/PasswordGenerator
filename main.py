import os
import random
import colorama
import pyperclip
from colorama import Fore

colorama.init(True)

# Variables
prefix = f"{Fore.RED}[UltraPW] "
white = f"{Fore.WHITE}"
yellow = f"{Fore.YELLOW}"
length_limit = 33
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "!@#$%&*()."
Combine = lower + upper + number + symbol

# Design
os.system('')
print(f"""{Fore.RED}

 ██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░
 ██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗
 ██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║
 ██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║
 ██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝
 ╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░
""")

print(f"{white}Password Generator 1.0 {Fore.GREEN}BETA{Fore.WHITE} Made By Mehran1022")
input("Press Enter To Continue...")
print("")

# Password Generation
passcode = int(input(prefix + white + "Your Password Length: "))
if passcode > length_limit:
    print(prefix + white + "You cannot enter numbers higher than 32.")
else:
    print(prefix + white + "Generating...")
    password = "".join(random.sample(Combine, passcode))
    print(prefix + white + "Your Password Is " + yellow + password)
    print("")
    copy = input(prefix + white + "Copy The Password Into Clipboard (y/n): ")
    if copy.lower() in {"y", "yes"}:
        pyperclip.copy(password)
        print(prefix + white + "Copied Successfully")
    else:
        print(prefix + white + "Terminating Tasks.")
