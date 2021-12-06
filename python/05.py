import math
testinput = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".split('\n')

with open("05.input", "r") as f:
  indata = f.read().split('\n')

def get_lines(data):
  return [[[int(p) for p in point.split(',')] for point in line.split(' -> ')] for line in data]

def is_straight(line):
  [x1, y1], [x2, y2] = line
  return x1 == x2 or y1 == y2

def is_diagonal(line, with_diagonal):
    if not with_diagonal:
      return False
    [x1, y1], [x2, y2] = line
    myradians = math.atan2(abs(y1-y2), abs(x1-x2))
    mydegrees = math.degrees(myradians)
    return int(mydegrees) == 45

def print_floor(floor):
  for y, row in enumerate(floor):
    print(y, row)

def render_line(line, floor):
  [x1, y1], [x2, y2] = line

  size = max(abs(x1 - x2), abs(y1 - y2))
  xdir = -1 if x1 - x2 > 0 else 1
  ydir = -1 if y1 - y2 > 0 else 1

  if x1 == x2:
    xdir = 0
  if y1 == y2:
    ydir = 0

  x, y = x1, y1
  floor[y][x] += 1
  for _ in range(0, size):
    x += xdir
    y += ydir
    floor[y][x] += 1

def get_intersections(with_diagonal = False):
  floor_size = 1000
  floor = [[0 for y in range(0,floor_size)] for x in range(0,floor_size)]
  # lines = [line for line in get_lines(indata) if is_straight(line) or is_diagonal(line, with_diagonal)]
  lines = [line for line in get_lines(indata)]

  for line in lines:
    render_line(line, floor)
  
  total = 0
  for row in floor:
    intersects = [num for num in row if num > 1]
    total += len(intersects)

  return total

part1 = get_intersections()
part2 = get_intersections(True)

print(part1)
print(part2)