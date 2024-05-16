graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = []

def dfs(visited,graph,node):
    if node not in visited:
        visited.append(node)
        print(node)
        for edge in graph[node]:
            dfs(visited,graph,edge)
            
            
            
dfs(visited,graph,'A')