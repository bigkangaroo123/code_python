def mean(nums):
    sum_of_nums = sum(nums)
    a = len(nums)
    mean = sum_of_nums / a
    return mean

def median(nums):
    a = sum(nums) - 1
    median = a / 2
    return nums[median]

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
