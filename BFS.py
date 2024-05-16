from collections import deque

def bfs(graph, start):
    print("The Nodes visited in BFS Method are:")
    visited = set()
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

                    
graph = {}
n = int(input("Enter the total number of nodes in the graph: "))
for i in range(n):   
    key = input("Enter the node: ")
    value = input("Enter it connecting edges: ").split()  
    if key in graph:
        graph[key].append(value)
    else:
        graph[key] = value

start = input("Enter the start node: ")

bfs(graph, start)