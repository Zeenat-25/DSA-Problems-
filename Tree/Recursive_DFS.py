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

    path.pop()      # Backtrack
    return None


start = 'A'
goal = 'F'

visited = []
path = []

result = dfs(graph, start, goal, visited, path)

if result:
    print("Path Found:", " -> ".join(result))
else:
    print("Path Not Found")
