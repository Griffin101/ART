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
goal = 'Bucharest'

def recursive_best_first_search(current_city, path_cost, f_limit):
    if current_city == goal:
        return [current_city], path_cost

    successors = [(neighbor, path_cost + cost + dict_hn[neighbor]) for neighbor, cost in dict_gn[current_city].items()]
    successors.sort(key=lambda x: x[1])  # Sort by total cost

    for successor, total_cost in successors:
        if total_cost > f_limit:
            return None, total_cost

        result_path, result_cost = recursive_best_first_search(successor, path_cost + dict_gn[current_city][successor], f_limit)
        if result_path is not None:
            return [current_city] + result_path, result_cost

    return None, float('inf')

def main():
    f_limit = float('inf')
    result_path, result_cost = recursive_best_first_search(start, 0, f_limit)

    if result_path:
        print(f"The Recursive Best-First Search path is: {result_path}")
        print(f"The total cost is: {result_cost}")
    else:
        print("No path found.")

if __name__ == "__main__":
    main()
