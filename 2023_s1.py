c = int(input())
top = list(map(int, input().split()))
bottom = list(map(int, input().split()))

tape_length = 0
for i in range(c):
    if top[i] == 1:
        tape_length += 3
    if bottom[i] == 1:
        tape_length += 3
    if i % 2 == 0:
        if top[i] == 1 and bottom[i] == 1:
            tape_length -= 2
    if i>0:
        if top[i] == 1 and top[i-1] == 1:
            tape_length -= 2
        if bottom[i] == 1 and bottom[i-1] == 1:
            tape_length -= 2

print(tape_length)