n = 6
graph = {
        5: [3, 7],  
        3: [2, 4],   
        7: [8],
        2: [],
        4: [8],
        8: []
    }
discovered = []
def DFS(graph, v, discovered):
    discovered.append(v)
    print(v, end=' ')            
    if v in graph:
        for u in graph[v]:
            if u not in discovered:      
                DFS(graph, u, discovered)
 
DFS(graph, 5, discovered)