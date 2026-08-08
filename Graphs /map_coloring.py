graph = {
    'A' : ['B','C'],
    'B' : ['A', 'C','D'],
    'C' : ['A','B','D'],
    'D' : ['B','C'],
}

colors = ['Red','Green','Blue']
assignment = {}

def is_safe(regoin, color):
    for neighbor in graph[regoin]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


def map_coloring():
  if len(assignment) == len(graph):
    return assignment
  for regoin in graph:
    if regoin not in assignment:
      for color in colors:
        if is_safe(regoin, color):
          assignment[regoin] = color

          if map_coloring():
            return assignment
            del assignment[region]
  return False


if map_coloring() :
  print("Map Coloring Solution")
  for region in assignment:
    print(region, "->", assignment[region])
else:
  print("No solution exists")

