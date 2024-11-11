import math

log_number = int(input(''))
log_from = int(input(''))

def log(log_number):
    a = 1
    print('-=-'*20)
    while log_number ** a <= log_from :
        print(log_number ** a)
        a = a + 1 
    
    print('-=-'*20)
    print(log_number)

log(log_number)