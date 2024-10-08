def insertSort(array):
    # Start from the second element (index 1)
    i = 1

    # If the array is empty, return an empty list
    if not array:
        return []
    # If the array has only one element, it's already sorted
    elif len(array) == 1:
        return array
    else:
        # Loop through each element in the array starting from index 1
        while i < len(array):
            j = i  # Set up j to point to the current element
            # Compare the current element with the previous elements
            while j > 0 and array[j-1] > array[j]:
                # If the previous element is greater, swap them
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp

                # Move to the previous element
                j -= 1
            # End of inner while loop, move to the next element
            i += 1
        # End of outer while loop
        return array

# End of insertSort()

# Test the function
test = [6, 5, 3, 1, 8, 7, 3, 4]
insertSort(test)  # Since it is a list, it will mutate it

# Print the sorted result
print('Sorted:', test)


#i tracks the position of the current element that is being inserted into the sorted portion of the array
#j compares the current element(at index i) with elements in the sorted portion of the array to the left of i
