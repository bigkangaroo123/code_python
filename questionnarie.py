from collections import Counter

n, m = map(int, input().split())
votings = []
t = n
while t:
    nums = list(map(int, input().split()))
    votings.append(nums)
    t-=1
choices = {i: 0 for i in range(1, m+1)}

for i in range(len(votings)):
    for j in range(len(votings[0])):
        if votings[i][j] == 1:
            choices[j+1] += 1

sorted_cands = [key for key, _ in Counter(choices).most_common()]
print(" ".join(map(str, sorted_cands)))