
# Given a tic tac toe board configuration, draw it out in the console out.
# Then determine whether there is a winning player.
# Example:
# [
#   ['X', '', 'O'],
#   ['', 'X', 'O'],
#   ['', '', 'X'],
# ]
#
# Should be rendered as:
# +---+---+---+
# | X |   | O |
# +---+---+---+
# |   | X | O |
# +---+---+---+
# |   |   | X |
# +---+---+---+
# Winning player: X

def render_row_separator():
  print('+---+---+---+')

def render_board_row(row):
  for marking in row:
    if not marking:
      marking = ' '
    print('| %s ' % marking, end='')
  print('|')

def render_board(board):
  for row in board:
    render_row_separator()
    render_board_row(row)
  render_row_separator()

# Assume number of rows == number of columns = 3

def get_winning_player_in_row(board, row_index):
  if board[row_index][0] == board[row_index][1] == board[row_index][2]:
    return board[row_index][0]
  return None

def get_winning_player_in_column(board, col_index):
  if board[0][col_index] == board[1][col_index] == board[2][col_index]:
    return board[0][col_index]
  return None

def get_winning_player_in_main_diagonal(board):
  if board[0][0] == board[1][1] == board[2][2]:
    return board[0][0]
  return None

def get_winning_player_in_anti_diagonal(board):
  if board[0][2] == board[1][1] == board[2][0]:
    return board[0][0]
  return None

def find_winning_player(board):
  winner = get_winning_player_in_main_diagonal(board)
  if winner:
    return winner

  winner = get_winning_player_in_anti_diagonal(board)
  if winner:
    return winner

  # Iterate by row and columns
  for i in range(3):
    winner = get_winning_player_in_row(board, i)
    if winner:
      return winner
    
    winner = get_winning_player_in_column(board, i)
    if winner:
      return winner

BOARD = [
  ['X', '', 'O',],
  ['', 'X', 'O'],
  ['', '', 'X'],
]

render_board(BOARD)
print("Winning player:", find_winning_player(BOARD))
