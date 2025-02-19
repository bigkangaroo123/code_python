n = int(input())
for _ in range(n):
    n1, n2 = input().split()

    if len(n1) >= 2 and n1[-2:] == "17":
        print("NO")
        continue
    if len(n2) >= 2 and n2[-2:] == "17":
        print("NO")
        continue
    if len(n2) >= 2:
        if n1[-1] == '7' and n2[-2:] == "11":
            print("YES")
            continue
    if len(n1) >= 2:
        if n2[-1] == '7' and n1[-2:] == "11":
            print("YES")
            continue

    print("NO")
