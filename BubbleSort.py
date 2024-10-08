def BubbleSort(array):
    swapped = True #initializing to run the loop in else
    
    if not array:
        return []
    elif len(array) == 1:
        return array
    else:
        while swapped:
            swapped = False
            #swapped turned to false because the indexes haven't swapped yet
            #its true when starting the loop cuz this loop actually swaps them, so swapped turns true
            for i in range(1, len(array)):
                if array[i-1] > array[i]:
                    temp = array[i-1]
                    array[i-1] = array[i]
                    array[i] = temp
                    swapped = True
                    #swapped set to true so that this loop runs again, as long as it sorts the whole thing

    return array
test = [4, 5, 9, 2, 6, 7, 1, 0]
sorted_array = BubbleSort(test)
print(sorted_array)
