numletter = {2:"ABC", 3:"DEF", 4:"GHI", 5:"JKL", 6:"MNO", 7:"PQRS", 8:"TUV", 9:"WXYZ"}
t = int(input())
for i in range(t):
    nums = input().replace("-", "") #416PIZZABOX
    if len(nums) > 10:
        nums = nums[:10]
    digits = []
    
    for char in nums:
        if char in numletter[2]:
            digits.append(2)
        elif char in numletter[3]:
            digits.append(3)
        elif char in numletter[4]:
            digits.append(4)
        elif char in numletter[5]:
            digits.append(5)
        elif char in numletter[6]:
            digits.append(6)
        elif char in numletter[7]:
            digits.append(7)
        elif char in numletter[8]:
            digits.append(8)
        elif char in numletter[9]:
            digits.append(9)
        else:
            digits.append(int(char))
    
    print("".join(map(str, digits[:3])) + "-" + "".join(map(str, digits[3:6])) + "-" + "".join(map(str, digits[6:])))