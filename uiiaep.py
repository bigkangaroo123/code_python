nums = [1, 3, 4, 5, 7, 9, 10]
left = 0
right = len(nums) - 1
target = 10
e = 0
f = 0
while True:
    if nums[left]+nums[right]== target:
        e = nums[left]
        f = nums[right]
        break
    elif nums[left]+nums[right] > target:
        right -= 1
    else:
        left += 1
print(e, f)