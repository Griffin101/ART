import queue as Q

dict_hn={'Arad':336,'Bucharest':0,'Craiova':160,'Drobeta':242,'Eforie':161,
'Fagaras':176,'Giurgiu':77,'Hirsova':151,'Iasi':226,'Lugoj':244,
'Mehadia':241,'Neamt':234,'Oradea':380,'Pitesti':100,
'Sibiu':253,'Timisoara':329,'Urziceni':80,'Vaslui':199,'Zerind':374}
dict_gn=dict(
Arad=dict(Zerind=75,Timisoara=118,Sibiu=140),
Bucharest=dict(Urziceni=85,Giurgiu=90,Pitesti=101,Fagaras=211),
Craiova=dict(Drobeta=120,Pitesti=138,),
Drobeta=dict(Mehadia=75,Craiova=120),
Eforie=dict(Hirsova=86),
Fagaras=dict(Sibiu=99,Bucharest=211),
Giurgiu=dict(Bucharest=90),
Hirsova=dict(Eforie=86,Urziceni=98),
Iasi=dict(Neamt=87,Vaslui=92),
Lugoj=dict(Mehadia=70,Timisoara=111),
Mehadia=dict(Lugoj=70,Drobeta=75),
Neamt=dict(Iasi=87),
Oradea=dict(Zerind=71,Sibiu=151),
Pitesti=dict(Bucharest=101,Craiova=138),
Sibiu=dict(Fagaras=99,Arad=140,Oradea=151),
Timisoara=dict(Lugoj=111,Arad=118),
Urziceni=dict(Bucharest=85,Hirsova=98,Vaslui=142),
Vaslui=dict(Iasi=92,Urziceni=142),
Zerind=dict(Oradea=71,Arad=75)
)

start = 'Arad'
goal = 'Vaslui'

result = []

def expand(city, cityq, path_cost):
    for neighbor, cost in dict_gn[city].items():
        total_cost = path_cost + cost + dict_hn[neighbor]
        cityq.put((total_cost, neighbor, total_cost - dict_hn[neighbor]))

def astar_search(start, goal):
    cityq = Q.PriorityQueue()
    cityq.put((dict_hn[start], start, 0))

    while not cityq.empty():
        current_hn, current_city, current_cost = cityq.get()
        result.append(current_city)

        if current_city == goal:
            print(f"The A* path is: {result}")
            print(f"The total cost is: {current_cost}")
            return

        expand(current_city, cityq, current_cost)

def main():
    astar_search(start, goal)

if __name__ == "__main__":
    main()
