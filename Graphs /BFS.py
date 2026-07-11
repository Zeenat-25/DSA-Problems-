# BFS
from collections import deque

graph = {
     'Oradea' : ['Zerind','Sibiu',],
     'Arad' : ['Sibiu' , 'Timisoara' , 'Zerind'],
     'Zerind' : ['Arad' , 'Oradea'],
     'Timisoara' : ['Lugoj' , 'Arad'],
     'Lugoj' : ['Mechadia','Timisoara'],
     'Mechadia' : ['Lugoj','Drobeta'],
     'Drobeta' : ['Mechadia' , 'Craiova'],
     'Craiova' : ['Drobeta' , 'Rimnicu Vilcea', 'Pitesti'],
     'Pitesti' : ['Craiova' , 'Rimnicu Vilcea' , 'Bucharest'],
     'Rimnicu Vilcea' : ['Pitesti' , 'Craiova' , 'Sibiu'],
     'Sibiu' : ['Arad' , 'Oradea' , 'Rimnicu Vilcea' , 'Fagaras'],
     'Fagaras' : ['Sibiu' , 'Bucharest'],
     'Bucharest' : ['Fagaras' , 'Pitesti' , 'Giurgiu' , 'Urziceni'],
     'Giurgiu' : ['Bucharest'],
     'Urziceni' : ['Bucharest' , 'Hirsova' , 'Vaslui'],
     'Hirsova' : ['Urziceni' , 'Eforie'],
     'Eforie' : ['Hirsova'],
     'Vaslui' : ['Urziceni' , 'Iasi'],
     'Iasi' : ['Vaslui' , 'Neamt'],
     'Neamt' : ['Iasi']


 }

def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = []

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.append(node)

            for neighbour in graph[node]:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

    return None   # <-- Outside the while loop

start = 'Oradea'
goal = 'Hirsova'

result = bfs(graph, start, goal)

if result:
    print("Path Found:", " -> ".join(result))
else:
    print("Path Not Found")
