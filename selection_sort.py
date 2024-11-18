def selectionsort(array, result=[]):
    if not array:
        return result
    else:
        smallest = array[0]
        s_index = 0
        for i in range(1, len(array)):
            if array[i] < smallest:
                smallest = array[i]
                s_index = i
                
        result.append(array.pop(s_index))

        return selectionsort(array, result)

a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])

print(selectionsort(a))
