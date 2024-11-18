def insertion(array):
    if not array or len(array) == 1:
        return array
    else:
        i = 1
        while i < len(array):
            j = i
            while j > 0:
                if array[j-1] > array[j]:
                    array[j-1] > array[j]
                    temp = array[j-1]
                    array[j-1] = array[j]
                    array[j] = temp
                j -= 1
            i += 1
        return array

a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
print(insertion(a))
