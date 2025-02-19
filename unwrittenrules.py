#M = N/2 seats onm each side
#all seats in teh same row ahead should be empty to leave
#all ppl closer to the aile have left
def rules(n, m, leave_order):
    seating = {}

    student = 1
    for row in range(n):
        for pos in range(m):
            seating[student] = (row, "L", pos)
            student += 1
        for pos in range(m):
            seating[student] = (row, "R", pos)
            student += 1
    
    l_cleared = -1
    r_cleared = -1
    last_p = {}

    for student in leave_order:
        row, g, pos = seating[student]

        if row > max(l_cleared, r_cleared):     
            return "no"
        
        if row in last_p and g in last_p[row]:
            if last_p[row][g] > pos:
                return "no"
            
        if row not in last_p:
            last_p[row] = {}
        last_p[row][g] = pos

        if g == "L":
            left_cleared_row = row
        else:
            right_cleared_row = row

    return "yes"
    

n, m = map(int, input().split())
leave_order = [int(input()) for _ in range(2 * n * m)]
print(rules(n, m, leave_order))
