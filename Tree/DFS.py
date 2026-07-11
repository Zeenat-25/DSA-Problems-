 graph = {
     'A' : ['B','C'],
     'B' : ['D', 'E'],
     'C' : ['F'],
     'D' : [],
     'E' : ['F'],
     'F' : []
 }

 def dfs(graph , start , goal) :
  stack = [[start]]
  visited = []
  while stack :
    path = stack.pop()
    node = path[-1]

    if node == goal :
      return path

    if node not in visited :
      visited.append(node)
      

      for neighbour in reversed(graph[node]) :
        new_path = list(path)
        new_path.append(neighbour)
        stack.append(new_path)
  
  return None


start = 'A'
goal = 'F'

result = dfs(graph , start , goal)

if result :
  print("Path Found : "," -> ", " -> ".join(result))
else :
  print("Path Not Found")
