from collections import defaultdict 
def iterative_dfs(graph, start):
    stack = [start] 
    visited = set() 
    while stack:
        current_node = stack.pop()
        if current_node not in visited: 
            print(current_node, end=" ") 
            visited.add(current_node)
            stack.extend(neighbor for neighbor in graph[current_node] if neighbor not in visited) 

graph = defaultdict(list) 

graph['A'] = ['B', 'C']

graph['B'] = ['D']

graph['C'] = ['E']

graph['D'] = []

graph['E'] = []

start_node = 'A'

print("IDFS Traversal:") 

iterative_dfs(graph, start_node)