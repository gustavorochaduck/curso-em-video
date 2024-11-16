
def binary_search(list, item):
    low = 0
    high = len(list)

    while low <= high:
        mid = (low + high) // 2
        guess = len(list) - 1

        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1
    
    return None

sequence = [1, 2, 6, 78 ,3, 7, 5, 8,]
item_a = 5

print(binary_search(sequence, item_a))