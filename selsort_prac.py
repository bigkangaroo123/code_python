def sel_sort(array, sorted_list = []):
    if not array:
        return sorted_list
    else:
        target = min(array)
        target_index = 0
        for i in range(len(array)):
            if array[i] == target:
                target_index = i
        sorted_list.append(target)
        array.pop(target_index)
        return sel_sort(array, sorted_list)
    
test = [5, 8, 2, 9, 4, 1]
print(sel_sort(test))