graph = {
    'Oradea': ['Zerind', 'Sibiu'],
    'Arad': ['Sibiu', 'Timisoara', 'Zerind'],
    'Zerind': ['Arad', 'Oradea'],
    'Timisoara': ['Lugoj', 'Arad'],
    'Lugoj': ['Mechadia', 'Timisoara'],
    'Mechadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mechadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
    'Pitesti': ['Craiova', 'Rimnicu Vilcea', 'Bucharest'],
    'Rimnicu Vilcea': ['Pitesti', 'Craiova', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Rimnicu Vilcea', 'Fagaras'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}

def dfs(graph, node, goal, visited, path):

    visited.append(node)
    path.append(node)

    if node == goal:
        return path

    for neighbour in graph[node]:
        if neighbour not in visited:
            result = dfs(graph, neighbour, goal, visited, path)
            if result:
                return result

    path.pop()
    return None


start = 'Oradea'
goal = 'Hirsova'

visited = []
path = []

result = dfs(graph, start, goal, visited, path)

if result:
    print("Path Found:", " -> ".join(result))
else:
    print("Path Not Found")
