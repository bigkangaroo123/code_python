def linear_search(array, target):
    i = 0
    while i < len(array):
        if array[i] == target:
            return target
        else:
            i += 1
    return f"target not found in the array"

def binary_search(array, target):
    array = sorted(array)
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            return target
        else:
            if array[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
    return f"target not found in the array"

def bubble_sort(array):
    sorted = True
    while sorted:
        sorted = False
        for i in range(1, len(array)):
            if array[i-1] > array[i]:
                temp = array[i-1]
                array[i-1] = array[i]
                array[i] = temp
                sorted = True
    return array

def insertion_sort(array): #array is [6, 8, 3, 4]
    i = 1
    while i < len(array):
        j = i
        while j > 0 and array[j-1] > array[j]:
            temp = array[j-1]
            array[j-1] = array[j]
            array[j] = temp
            j -= 1
        i += 1
    return array

def selection_sort(array, sorted=[]):
    if not array:
        return sorted
    else:
        least = min(array)
        array.remove(least)
        sorted.append(least)
        return selection_sort(array, sorted)
    
test = [5, 9, 3, 7, 6, 4, 8, 0, 2, 1]
print(binary_search(test, 8))

