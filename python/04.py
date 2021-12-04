testinput = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

def get_boards(input):
  items = input.split('\n\n')
  return [items[0].split(','), [[rowstr.split() for rowstr in row.split('\n')] for row in items[1:]]]

with open("04.input", "r") as f:
    input = f.read()

def check_board(numbers, board):
  for colidx in range(0, 5):
    check_col = all([num[colidx] in numbers for num in board])
    if(check_col):
      return True
  
  for row in board:
    check_row = all([num in numbers for num in row])
    if(check_row):
      return True
  return False

def get_numbers(board, numbers_played):
  result = []
  for row in board:
    non_played_numbers = [int(num) for num in row if num not in numbers_played]
    result += non_played_numbers
  return result

def play_bingo(first = True):
  numbers, boards = get_boards(input)
  winning_boards = []
  for idx, num in enumerate(numbers):
    for bid, board in enumerate(boards):
      is_winner = check_board(numbers[:idx + 1], board)
      if(is_winner and first):
        return sum(get_numbers(board, numbers[:idx + 1])) * int(num)
      if(is_winner and bid not in winning_boards):
        winning_boards.append(bid)
        if(len(winning_boards) == len(boards)):
          return sum(get_numbers(board, numbers[:idx + 1])) * int(num)

total = play_bingo()
total2 = play_bingo(False)
print(total)
print(total2)