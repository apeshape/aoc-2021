import time

# input = """5483143223
# 2745854711
# 5264556173
# 6141336146
# 6357385478
# 4167524645
# 2176841721
# 6882881134
# 4846848554
# 5283751526""".split('\n')

input = """1326253315
3427728113
5751612542
6543868322
4422526221
2234325647
1773174887
7281321674
6562513118
4824541522""".split('\n')

def get_value(point, grid):
  return grid[point[0]][point[1]]

def find_neighbours(point, grid):
  dirs = [(0,-1), (1,-1), (1,0), (1,1), (0,1), (-1, 1), (-1,0), (-1, -1)]
  neighbours = []
  for dir in dirs:
    testpoint = (point[0] + dir[0], point[1] + dir[1])
    try:
      if testpoint[0] >= len(grid[0]) or testpoint[0] < 0 or testpoint[1] > len(grid) - 1 or testpoint[1] < 0:
        neighbours.append('-')
      else:
        neighbours.append(testpoint)
    except IndexError:
      neighbours.append('-')
  
  return neighbours

def get_colored(n):
  if n == 0:
    return '\033[1;31m ' + str(n)
  return '\033[1;32m ' + str(n)

def print_grid(grid):
  print(chr(27)+'[2j')
  print('\033c')
  print('\x1bc')
  for line in grid:
    strline = [get_colored(n) for n in line]
    print(''.join(strline))
  
  print('-' * len(grid[0]))

def flash(squid, has_flashed, grid):
  if squid in has_flashed:
    return has_flashed
  has_flashed.append(squid)
  neighbours = [n for n in find_neighbours(squid, grid) if n != '-']

  for n in neighbours:
    grid[n[0]][n[1]] += 1
    if get_value(n, grid) > 9:
      flash(n, has_flashed, grid)
  
  return has_flashed
  
def reset_flashed(flashed, grid):
  for f in flashed:
    grid[f[0]][f[1]] = 0

def do_turn(grid):
  has_flashed = []
  flashed = []
  for x, char in enumerate(grid[0]):
    for y, row in enumerate(grid):
      grid[x][y] += 1

      if get_value((x,y), grid) > 9:
        flashed = flash((x,y), has_flashed, grid)
  reset_flashed(flashed, grid)

  return len(flashed)

def all_flashed(grid):
  return all([r == 0 for sub in grid for r in sub])


def part1():
  grid = [list(map(int,list(row))) for row in input]
  total = 0
  for _ in range(0,100):
    total += do_turn(grid)
    # print_grid(grid)
    # time.sleep(0.2)
  return total

def part2():
  grid = [list(map(int,list(row))) for row in input]
  turns = 0
  while not all_flashed(grid):
    do_turn(grid)
    turns += 1

  return turns

print(part1())
print(part2())
