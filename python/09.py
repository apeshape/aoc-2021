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
  dirs = [(0,-1), (1,0), (0,1), (-1,0)]
  neighbours = []
  for dir in dirs:
    testpoint = (point[0] + dir[0], point[1] + dir[1])
    try:
      if testpoint[0] >= len(hmap[0]) or testpoint[0] < 0 or testpoint[1] > len(hmap) - 1 or testpoint[1] < 0:
        neighbours.append('-')
      else:
        neighbours.append(testpoint)
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

def part1():
  lowest = []
  for y, row in enumerate(hmap):
    for x, col in enumerate(row):
      neighbours = find_neighbours((x, y))

      if all([int(col) < int(get_value(n)) for n in neighbours if n != '-']):
        lowest.append(int(get_value((x, y))) + 1)
  return sum(lowest)

def part2():
  basin_lengths = []
  for y, row in enumerate(hmap):
    for x, col in enumerate(row):
      neighbours = find_neighbours((x, y))

      if all([int(col) < int(get_value(n)) for n in neighbours if n != '-']):
        points = get_basin((x, y), [(x, y)])
        basin_lengths.append(len(points))
  basins = sorted(basin_lengths)
  total = math.prod(basins[-3:])
  return total

print(part1())
print(part2())