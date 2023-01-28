# Packages

import os
import time
import random
import colorama
import clipboard
import pyperclip
from colorama import Fore
colorama.init(True)


print('')
# Things

prefix = f"{colorama.Fore.RED}[UltraPW] "
white = f"{colorama.Fore.WHITE}"
yellow = f"{colorama.Fore.YELLOW}"
lenght_limit = 33
lower = "abcdefghijklmnopqrstuvwxyz"
upper =  "ABCDEFGHIGKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "!@#$%&*()."
Combine = lower + upper + number + symbol

# Design

os.system('')
print(f"""{colorama.Fore.RED}
        
        
        

 ██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░
 ██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗
 ██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║
 ██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║
 ██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝
 ╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░
        """)
print("")
print(white + f"Password Generator 1.0 {Fore.GREEN}BETA{Fore.WHITE} Made By Mehran1022")
print("")
input("Press Enter To Countinue...")
print("")
passcode = int(input(prefix + white + "Your Password Length: "))
print(prefix + white + "Generating...")
time.sleep(2.5)
password = "".join(random.sample(Combine, passcode))

# Generation Options

if lenght_limit > passcode:
  print(prefix + white +"Your Password Is " + yellow + password)
  print('')
  time.sleep(1.5)
  copy = str(input(prefix + white + "Copy The Password Into Clipboard (y/n): "))
  if copy == 'y' or copy == 'yes':
    clipboard.copy(password)
    time.sleep(1)
    print(prefix + white + "Copied Successfully")
  else:
    print(prefix + white + "Terminatig Tasks.")
    
else:
    print(prefix + white + "You Cannot Enter Numbers Higher Than 32.")

# Program Loop

#print("")
# end = str(input(prefix + white + "Close The App? : "))
#if end == "yes" or end == "y" or end == "Y":
#  code()
# if end == 'n' or end == 'no':
#  print(prefix + white + "Terminating The Script...")