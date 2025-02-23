from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)

x, y = map(int, input().split())

def can_reach(start, target):
    visited = [0 for _ in range(n + 1)]
    queue = deque([start])
    visited[start] = 1

    while queue:
        node = queue.popleft()

        if node == target:
            return True
        for e in graph[node]:
            if visited[e]:
                continue
            visited[e] = 1
            queue.append(e)
    return False

if can_reach(x, y):
    print("yes")
elif can_reach(y, x):
    print("no")
else:
    print("unknown")















"""
main function pseudocode:

create a queue starting from the x value of the final comparison

create empty set to keep track of visited nodes (and avoid infiite loops)

while queue is not empty:
    take first element from the queue
    check if it is equal to the target(y value of the comparison)
        if yes, output "yes"
        else:
        put that in visited 
    
        check if that element has any neighbours in the graph
        if graph[5] exists, we add all those y values to the queue (extending the path)
        if graph[5] is [], we don't add anything to the queue.

    if queue is empty, loop ends, no path found, return false
    output "no"

"""



