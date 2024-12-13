import sys
from time import sleep

def typewrite_animation(words):
    for char in words:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()


typewrite_animation("Welcome to the ADM Software!!!")
print("")
typewrite_animation("Select a Option:")
print("")
print("[1] - Open the command line")
print("[2] - SHOW")
print("[3] - UPDATE")
print("[4] - REMOVE")
print("[5] - ADD")
print(")")
selection = int(input("Digit: "))

if selection == 1:
    print("log")



