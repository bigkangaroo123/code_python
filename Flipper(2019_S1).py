#1 2
#3 4

input_joint = input().strip()
inputs = input_joint.split()

nums = [1, 2, 3, 4]
for i in inputs:
    if i == "H":
        nums[0], nums[2] = nums[2], nums[0]
        nums[1], nums[3] = nums[3], nums[1]
    elif i == "V":
        nums[0], nums[1] = nums[1], nums[0]
        nums[2], nums[3] = nums[3], nums[2]

print(nums[0], nums[1])
print(nums[2], nums[3])
