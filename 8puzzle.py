def print_board(board):
  for row in board:
    print(row)
  print()
def find_blank(board):
  for i in range(3):
    for j in range(3):
      if board[i][j] == 0:
        return i, j

def generate_moves(board) :
  x,y = find_blank(board)

  moves = [(-1,0),(1,0),(0,-1),(0,1)]
  successors = []
  
  for dx,dy in moves :
    nx, ny = x+dx , y + dy

    if 0 <= nx < 3 and 0 <= ny < 3 :
      new_board = [row[:] for row in board]
      new_board[x][y] , new_board[nx][ny] =  new_board[nx][ny] , new_board[x][y]

      successors.append(new_board)

  return successors

board = [
    [1,2,3],
    [4,0,6],
    [7,8,5]
]

print("Initial Board")
print_board(board)

print("Possible Next States : ")

for state in generate_moves(board) :
  print_board(state)
