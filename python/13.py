import re
input = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

with open("13.input", "r") as f:
  input = f.read()


point_lines, fold_lines = input.split('\n\n')

points = [list(map(int, p.split(','))) for p in point_lines.split('\n')]
folds = [re.findall(r'([x|y])=(\d+)', fold)[0] for fold in fold_lines.split('\n')]
folds = [[fold[0], int(fold[1])] for fold in folds]

grid_size = (max([point[0] for point in points]) + 1, max([point[1] for point in points]) + 1)

grid = [['.' for x in range(grid_size[0])] for y in range(grid_size[1])]
for point in points:
  x, y = point
  grid[y][x] = '#'

def print_grid(g):
  for row in g:
    print(''.join(row))

def fold_grid(fold, g):
  axis, offset = fold
  fold = []

  if axis == 'y':
    fold_top = [row for idx, row in enumerate(g) if idx < offset]
    fold_bottom = list(reversed([row for idx, row in enumerate(g) if idx > offset]))

    for y, row in enumerate(fold_bottom):
      for x, col in enumerate(fold_bottom[y]):
        if fold_bottom[y][x] == '#':
          fold_top[y][x] = '#'
    
    return fold_top
  if axis == 'x':
    fold_left = [[col for idx, col in enumerate(row) if idx < offset] for row in g]
    fold_right = [[col for idx, col in enumerate(row) if idx > offset] for row in g]
    fold_size = (len(fold_left[0]) - 1, len(fold_left) - 1)

    for y, row in enumerate(fold_right):
      for x, col in enumerate(fold_right[y]):
        if fold_right[y][x] == '#':
          fold_left[y][fold_size[0] - x] = '#'

    return fold_left

def part1():
  g = [row for row in grid]
  folded = fold_grid(folds[0], g)
  total = 0
  for row in folded:
    total += ''.join(row).count('#')
  print(total)

def part2():
  g = [row for row in grid]
  for fold in folds:
    g = fold_grid(fold, g)

  print_grid(g)

part1()
part2()