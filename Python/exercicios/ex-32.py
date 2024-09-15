from datetime import date

selection = int(input('Type the year or type 0 for the system year: '))

if selection == 0:
    selection = date.today().year
if selection > 0:
    if selection % 4 == 0 and selection % 10 != 0 or selection % 400 == 0:
        print(f'{selection} - This is a Leap Year!')
    else:
        print(f'{selection} - This is not a Leap Year.')
