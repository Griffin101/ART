import queue as Q

start = 'A'
goal = 'D'
result = ''

dict_hn = {'A': 20, 'B': 10, 'C': 5, 'D': 0}

dict_gn = {
    'A': {'B': 10},
    'B': {'C': 5, 'D': 10},
    'C': {'D': 5},
    'D': {}
}

def get_fn(nodestr):
    nodes = nodestr.split(" , ")
    hn = gn = 0
    for ctr in range(0, len(nodes)-1):
        gn = gn + dict_gn[nodes[ctr]][nodes[ctr + 1]]
    hn = dict_hn[nodes[len(nodes)-1]]
    return hn + gn

def expand(nodeq):
    global result
    tot, nodestr, thisnode = nodeq.get()
    if thisnode == goal:
        result = nodestr + " : : " + str(tot)
        return
    
    for node in dict_gn[thisnode]:
        nodeq.put((get_fn(nodestr + " , "+ node), nodestr + " , "+node, node))
    
    expand(nodeq)

def main():
    nodeq = Q.PriorityQueue()
    thisnode = start
    nodeq.put((get_fn(start), start, thisnode))
    expand(nodeq)
    print("The A* path with the total is: ")
    print(result)

main()