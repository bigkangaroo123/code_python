def bubbleSort(roomnums):
    swapped = True
    #memorize ts
    while swapped:
        swapped = False
        for i in range(1, len(roomnums)):
            if roomnums[i-1] > roomnums[i]:
                temp = roomnums[i-1]
                roomnums[i-1] = roomnums[i]
                roomnums[i] = temp
                swapped = True

    numsroom = roomnums[::-1]
    return numsroom

def check(roomnums):
    x = int(input("which room number u wanna check?: "))
    if x < 1 or x > 1000:
        return "invalid room number"
    elif x not in roomnums:
        return "not paid bill"
    else:
        return "paid bills"
roomnums = [2, 216, 15, 109, 156, 120, 93, 18, 21, 56]
print(check(roomnums))
print(f"sorted array: {bubbleSort(roomnums)}")

'''2 types of searching algorithms:
    linear search: searches sequentially in any list
    binary search: requires a sorted list to being with, but is more efficient
'''

'''characteristics of a linear array:
    - fixed size
    - sequential - allows for faster search techniques
'''
