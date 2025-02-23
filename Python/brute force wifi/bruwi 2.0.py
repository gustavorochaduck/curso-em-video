import os
import string
import subprocess
cmd = subprocess.Popen('cmd.exe')

char = string.ascii_letters + string.digits + string.punctuation
max_length = 64

def ssid_confirmation_win():
    print(os.popen("ipconfig").read())

def algorythm():
    for length in range(1, max_length+1):
        for guess in intertools.product(chars, repeat=length):
            attempt = "".join(guess)
            if attempt == ssid_confirmation:
                print(f'The password: {attempt}')
                input('Type to Close !!!')
                break

ssid_confirmation_win()