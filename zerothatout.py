lim = int(input())

nums = []

while lim:
    lim-=1
    inp = int(input())
    if inp == 0 and len(nums) > 0:
        nums.pop()
    else:
        nums.append(inp)

print(sum(nums))