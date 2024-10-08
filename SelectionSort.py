def selectSort(array, result=[]):
    # Check if the input list is empty
    if not array:
        # If it is, return the sorted result
        return result
    else:
        # Start by assuming the first element is the smallest
        smallest = array[0]
        small_index = 0

        # Loop through the rest of the list to find the smallest element
        for i in range(1, len(array)):
            if array[i] < smallest:
                # Update smallest and its index if a smaller element is found
                smallest = array[i]
                small_index = i

        # Remove the smallest element from the original list and add it to the result
        result.append(array.pop(small_index))

        # Recursively call selectSort with the updated list
        return selectSort(array, result)

# Test the sorting function with a sample list
test = [6, 5, 3, 1, 8, 7, 3, 4]
sorted_test = selectSort(test)  # This creates and returns a new sorted list

# Print the sorted list
print('Sorted:', sorted_test)
