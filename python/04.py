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

def test_board(board):
  cols = []
  for row in board:
    if ''.join(row) == 'XXXXX':
      return True
  
  for col in range(0, 5):
    collist = []
    for row in range(0,5):
      collist.append(board[row][col])
    cols.append(collist)

  for colrow in cols:
    if ''.join(colrow) == 'XXXXX':
      return True
  return False

def get_numbers(board):
  numbers = []
  for row in board:
    for col in row:
      if col != 'X':
        numbers.append(int(col))
  return numbers

def mark_number(num, board):
  for idx, row in enumerate(board):
    for jdx, rownum in enumerate(row):
      if str(num) == rownum:
        board[idx][jdx] = 'X'

def part1():
  numbers, boards = get_boards(input)
  winning_board = None
  winning_number = None
  for num in numbers.split(','):
    for board in boards:
      mark_number(num, board)
      if(test_board(board)):
        winning_board = board
        winning_number = num
        break
    if winning_board:
      break
  return int(winning_number) * sum(get_numbers(winning_board))


def print_board(board):
  for row in board:
    print(','.join(row) + '\n')

def part2():
  numbers, boards = get_boards(input)
  winners = []
  for num in numbers.split(','):
    for idx, board in enumerate(boards):
      if idx in winners:
        continue
      
      mark_number(num, board)
      if(test_board(board)):
        winners.append(idx)
        winning_number = num

  return int(winning_number) * sum(get_numbers(boards[int(winners[-1])]))


def new_check(numbers, board):
  # print('numbers::', numbers)
  # print('-- board --')
  # print(board)
  for colidx in range(0, 5):
    check_col = all([num[colidx] in numbers for num in board])
    if(check_col):
      return True
  
  for row in board:
    check_row = all([num in numbers for num in row])
    if(check_row):
      return True
  return False

def get_numbers_2(board, numbers_played):
  result = []
  print(numbers_played)
  for row in board:
    non_played_numbers = [int(num) for num in row if num not in numbers_played]
    result += non_played_numbers
  
  return result

def play_bingo(first = True):
  numbers, boards = get_boards(input)
  winning_boards = []
  for idx, num in enumerate(numbers):
    for bid, board in enumerate(boards):
      is_winner = new_check(numbers[:idx + 1], board)
      if(is_winner and first):
        return sum(get_numbers_2(board, numbers[:idx + 1])) * int(num)
      if(is_winner and bid not in winning_boards):
        winning_boards.append(bid)
        if(len(winning_boards) == len(boards)):
          print(len(winning_boards), sum(get_numbers_2(board, numbers[:idx + 1])), num)
          return sum(get_numbers_2(board, numbers[:idx + 1])) * int(num)


# numbers, boards = get_boards(testinput)
# nums = get_numbers_2(boards[0], ['22','13','17', '3', '18','15'])

# print(nums)

total = play_bingo()
total2 = play_bingo(False)
print(total2)

# print(part1())
# print(part2())
