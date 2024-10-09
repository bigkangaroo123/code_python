'''sum = sum(list of scores)
    divider = length of the list of scores
    average score = sum / divider
'''

'''for i in list:
    if i > average score:
        print(names[i], score[i])
'''

'''binary search code:
    left = 0
    right = len(list) - 1
    mid = (left + right) / 2

    if list[mid] < target:
        left = mid + 1
    elif list[mid] > target:
        right = mid - 1
    else:
        return mid (as it will be the target)
'''
def bin_search(array, target):
    left = 0
    right = len(names) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1
        else:
            return mid

names = ["Adams, Lana", "Allen, Mary", "Baker, Lilly", "Brown, Tea", "Fox, Tea", "Labar, Tanya", "Lee, Mae", "Miller, Ann", "Palmer, Ann", "Wood, Sarah"]
scores = [7.8, 6.5, 5.4, 9.2, 6.2, 8.5, 8.8, 5.1, 6.4, 9.1]
target = input("Which gymnast are you looking for? ex:(Lastname, Firstname): ")
index = 0
if target not in names:
    print("No such name found")
else:
    index = bin_search(names, target)
    print(f"The gymnast you're looking for has a score of {scores[index]}")

    
