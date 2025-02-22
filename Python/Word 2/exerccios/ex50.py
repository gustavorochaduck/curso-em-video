some = 0
count = 0

for x in range(1, 7):
    num = int(input('Type a Number: '))
    if num % 2 == 0:
        some += num
        count += 1

print(f'\nThe numbers Some are: {some}')