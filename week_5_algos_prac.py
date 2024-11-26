def selection_sort(array, sorted=[]):
    if not array:
        return sorted
    else:
        least = min(array)
        array.remove(least)
        sorted.append(least)
        return selection_sort(array, sorted)
    
test = [5, 9, 3, 7, 6, 4, 8, 0, 2, 1]
print(selection_sort(test))

