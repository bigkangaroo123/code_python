print("Enter names")
names = []
while True:
    name = input()
    names.append(name)
    if name == "x" or name == "X":
        break

longest_name = ""
for i in names: #if the list is of strings, the variable will automatically be a string so names[i] wouldnt work
    if len(i) > len(longest_name):
        longest_name = i

print("The longest name in this list is", longest_name)
