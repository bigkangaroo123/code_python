def string_compression(arg):
    compressed = []
    count = 0
    for i in range(len(arg)):
        count += 1 #char will be appearing at least once so start w/ 1
        # i + 1 == len to ensure if we are at the last character and we append it to compressed list
        if i + 1 == len(arg) or arg[i] != arg[i + 1]:
            compressed.append(arg[i] + str(count))
            count = 0 #reset count for next value
        #basically, this if statement checks what makes something not add to the compressed list and adds everything that's before, which is valid
    str_compressed = ''.join(compressed)
    return arg if len(str_compressed) > len(arg) else str_compressed

input_string = input("Enter whatever string: ")
str_comp = string_compression(input_string)
print(str_comp)
