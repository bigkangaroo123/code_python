x = int(input())
same = set()

if x > 0:
    for i in range(x):
        s1, s2 = input().split()
        same.add((s1, s2))

y = int(input())
diff = set()
if y > 0:
    for i in range(y):
        s1, s2 = input().split()
        diff.add((s1, s2))

g = int(input())
groups = {}

for group_id in range(g):
    s1, s2, s3 = input().split()
    groups[s1] = group_id
    groups[s2] = group_id
    groups[s3] = group_id

violated = 0
for s1, s2 in same:
    if groups[s1] != groups[s2]:
        violated += 1

for s1, s2 in diff:
    if groups[s1] == groups[s2]:
        violated += 1

print(violated)
