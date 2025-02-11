def possible_swipe(a, b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return 


n = int(input())
a = list(map(int, input().split()))  # [3, 1, 2]
b = list(map(int, input().split()))  # [3, 1, 1]