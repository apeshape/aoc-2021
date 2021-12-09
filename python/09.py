import math

# input = """2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678""".split('\n')

with open("09.input", "r") as f:
  input = f.read().split('\n')

hmap = [list(row) for row in input]


def find_neighbours(point):
    wall = '-'
    try:
      if point[1] - 1 < 0:
        above = wall
      else:
        above = (point[0], point[1] - 1)
    except IndexError:
      above = wall
    
    try:
      if hmap[point[1]][point[0] + 1]:
        right = (point[0] + 1, point[1])
      else:
        right = wall
    except IndexError:
      right = wall
    
    try:
      if hmap[point[1] + 1][point[0]]:
        below = (point[0], point[1] + 1)
      else:
        below = wall
    except IndexError:
      below = wall
    
    try:
      if point[0] - 1 < 0:
        left = wall
      else:
        left = (point[0] - 1, point[1])
    except IndexError:
      left = wall
    return [above, right, below, left]

def new_find_neighbours(point):
  dirs = [(0,-1), (1,0), (0,1), (-1,0)]
  neighbours = []
  for dir in dirs:
    # print(dir, point[0] + dir[0], point[1] + dir[1])
    testpoint = (point[0] + dir[0], point[1] + dir[1])
    try:
      if testpoint[0] > len(hmap) or testpoint[0] < 0 or testpoint[1] > len(hmap) or testpoint[1] < 0:
        neighbours.append('-')
      else:
        neighbours.append(testpoint)
      # v = hmap[point[1] + dir[0]][point[0] + dir[1]]
    except IndexError:
      neighbours.append('-')
  
  return neighbours

def get_value(point):
  return hmap[point[1]][point[0]]

def get_basin(start_point, found = []):
  neighbours_inbasin = [n for n in find_neighbours(start_point) if n != '-' and n not in found and get_value(n) != '9']

  if(len(neighbours_inbasin) == 0):
    return found

  found += neighbours_inbasin

  for n in neighbours_inbasin:
    get_basin(n, found)

  return found



lowest = []
basin_lengths = []
for y, row in enumerate(hmap):
  for x, col in enumerate(row):
    neighbours = find_neighbours((x, y))
    if all([int(col) < int(hmap[n[1]][n[0]]) for n in neighbours if n != '-']):
      points = get_basin((x, y), [(x, y)])
      basin_lengths.append(len(points))


# print(new_find_neighbours((99,99)))
# print(find_neighbours((99,99)))


basins = sorted(basin_lengths)
total = math.prod(basins[-3:])
print(total)

