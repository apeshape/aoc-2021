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

# input = """5483
# 2745
# 5264
# 6141""".split('\n')

# input = """11111
# 19991
# 19191
# 19991
# 11111""".split('\n')

grid = [list(map(int,list(row))) for row in input]

def get_value(point):
  return grid[point[0]][point[1]]

def find_neighbours(point):
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

def print_grid():
  for line in grid:
    print(line)
  
  print('-' * len(grid[0]))

def light_up(to_light, lit):
  for squid in to_light:
    grid[squid[0]][squid[1]] = 0
    lit.append((squid[0], squid[1]))

    # print('TO LIGHT:', to_light)

    # neighbours = [n for n in find_neighbours(squid) if n != '-' and n not in to_light and n not in lit]
    neighbours = [n for n in find_neighbours(squid) if n != '-']
    # print('neighbours', [(n, get_value(n)) for n in neighbours])

    tl = []
    for n in neighbours:
      grid[n[0]][n[1]] += 1
      val = get_value(n)
      if val > 9:
        # print('light up', n, val)
        # light_up([n], lit)
        tl.append(n)

    if len(tl) > 0:
      light_up(tl, lit)

def flash(squid, has_flashed):
  if squid in has_flashed:
    return has_flashed
  has_flashed.append(squid)
  neighbours = [n for n in find_neighbours(squid) if n != '-']

  for n in neighbours:
    grid[n[0]][n[1]] += 1
    # if n == (2,2):
    #   print('2,2', get_value(n))
    if get_value(n) > 9:
      # print('FLASH NEIGHBOUR', n, get_value(n), has_flashed)
      flash(n, has_flashed)
  
  return has_flashed
  
def reset_flashed(flashed):
  for f in flashed:
    grid[f[0]][f[1]] = 0

def do_turn():
  has_flashed = []
  flashed = []
  for x, char in enumerate(grid[0]):
    for y, row in enumerate(grid):
      grid[x][y] += 1

      val = grid[x][y]
      if val > 9:
        flashed = flash((x,y), has_flashed)
  print(flashed)
  reset_flashed(flashed)

  return len(flashed)
  # light_up(to_light, lit)

def all_flashed():
  return all([r == 0 for sub in grid for r in sub])


# print_grid()
# total = 0
# for turn in range(0,195):
#   print('TURN {t} ---->'.format(t=turn + 1))
#   total += do_turn()
# print_grid()
# print(total)

turns = 0
while not all_flashed():
  do_turn()
  turns += 1

print('total turns', turns)
print_grid()


# print(lit)