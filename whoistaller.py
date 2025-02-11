# 2 ppl back to back to determine the taller one
# the 2 height being compared cant be the same


def can_reach(start, target, graph):
    queue = [start]
    visited = set()

    while queue:
        node = queue.pop(0)

        if node == target:
            return True
        if node in visited:
            continue
        visited.add(node)

        if node in graph:
            queue.extend(graph[node])
    
    return False

n, m = map(int, input().split())

graph = {} #this dict. contains who is taller than who

for _ in range(m):
    x, y = map(int, input().split())

    if x not in graph:

        graph[x] = [] #creating empty lists if there are no comparisons stored for that x value in the graph

    graph[x].append(y) # Add y to x's list (meaning x is taller than y)
x, y = map(int, input().split())

if can_reach(x, y, graph):
    print("yes")
else:
    print("no")


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



