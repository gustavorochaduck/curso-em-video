number_1 = int(input('Type one number:'))
number_2 = int(input('Type one number:'))
number_3 = int(input('Type one number:'))

# Number one
if number_1 > number_2 and number_1 > number_3:
    print(f'{number_1} - This is the Largest Number')
elif number_1 < number_2 and number_1 < number_3:
    print(f'{number_1} - This is the Smallest Number')
else:
    print(f'{number_1} - You typed somthing wrong!')

# number two
if number_2 > number_1 and number_2 > number_3:
    print(f'{number_2} - This is the Largest Number')
elif number_2 < number_1 < number_3:
    print(f'{number_2} - This is the Smallest Number')
else:
    print(f'{number_2} - You Typed somthing wrong!')

# Number Three
if number_3 > number_1 and number_3 > number_2:
    print(f'{number_3} - This is The largest Number')
elif number_3 < number_1 and number_3 < number_2:
    print(f'{number_3} - This is the Smallest Number')
