vals = []
for _ in range(6):
    val_tup = tuple(map(float, input().split()))
    vals.append(val_tup)

deno = len(vals)
sum = 0
unc = 0
for i in vals:
    sum = sum + i[0]
    unc = unc + i[1]

average = sum / 6
unc_final = average* (unc/sum)

print(average,"+-",unc_final)