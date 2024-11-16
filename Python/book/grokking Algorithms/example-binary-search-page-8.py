item_to_search = 7

sequence = [1, 3, 5, 7, 9]
#You need to know the list commands

def binary_search(list, item_to_search):
    high = len(list) - 1
    low = 0

    while low <= high:
        mid = (low + high) / 2
        guess = list(mid)

        if guess == item_to_search:
            return mid
        elif guess > item_to_search:
            high = mid - 1 
        else:
            low = mid -1
    
    return none

print(binary_search(sequence, item_to_search))