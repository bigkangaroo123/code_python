def mean(nums):
    return sum(nums) / len(nums)

def median(nums):
    nums = sorted(nums)
    if len(nums) / 2 >= 1:
        return nums[len(nums / 2)]
    else:
        middle1 = nums[len(nums) / 2 - 1]
        middle2 = nums[len(nums) / 2]
        return (middle1 + middle2) / 2

print("Enter numbers: (enter X to stop)")
nums = []
while True:
    a = input()
    if a == "X" or a == "x":
        break
    else:
        b = int(a)
        nums.append(b)

mean_or_median = print("Want to find mean or median?")
if mean_or_median == "Mean":
    mean = mean(nums)
else:
    median = median(nums)
