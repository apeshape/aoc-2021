from re import findall
from grid import print_grid

input = "target area: x=20..30, y=-10..-5"
input = "target area: x=155..182, y=-117..-67"

sizestrs = input.split(': ')[1].split(', ')

target_sizes = {}
for sizestr in sizestrs:
  axis, positions = sizestr.split('=')
  sizes = [int(x) for x in findall(r"(-?\d+)..(-?\d+)", positions)[0]]
  target_sizes[axis] = {"max": max(sizes), "min": min(sizes), "size": abs(sizes[0] - sizes[1]) + 1}

def get_grid():
  grid_size = (target_sizes['x']['max'] + 1, abs(target_sizes['y']['min']) + 1)

  grid = [['.' for x in range(grid_size[0])] for y in range(grid_size[1])]

  zero_y = 0

  grid[zero_y][0] = 'S'

  # set target
  for tx in range(target_sizes['x']['size']):
    for ty in range(target_sizes['y']['size']):
      grid[(abs(target_sizes['y']['max']) + zero_y) + ty][(target_sizes['x']['min']) + tx] = 'T'
  
  return grid

def expand_grid_by(y, g):
  expansion = []
  for _ in range(y):
    expansion.append(['.' for x in range(len(g[0]))])

  new_grid = [*expansion, *g]
  return new_grid


def update(current_pos, velocity):
  currx, curry = current_pos
  velx, vely = velocity
  newx = currx + velx
  newy = curry - vely

  velxchange = -1 if velx > 0 else 0

  return (newx, newy), (velx + velxchange, vely - 1)


def get_grid_pos(pos, start_y):
  grid_pos = (pos[0], pos[1] + start_y)
  return grid_pos

def test_velocity(velocity, grid_size, highest=False):
  start_y = 0
  current_pos = (0, start_y)
  hitormiss = False
  start_velocity = velocity
  highest_y = 0
  # grid = get_grid()

  while not hitormiss:
    current_pos, velocity = update(current_pos, velocity)
    curx, cury = current_pos

    if cury < highest_y:
      start_y = abs(cury)
      # grid = expand_grid_by(abs(cury) + highest_y, grid)

      highest_y = cury

    gridx, gridy = get_grid_pos(current_pos, start_y)

    if gridx >= grid_size[0] or gridy >= grid_size[1] + start_y:
      # Miss
      hitormiss = True
      break
    
    if gridx >= target_sizes['x']['min'] and gridx <= target_sizes['x']['max'] and gridy <= (abs(target_sizes['y']['min']) + start_y) and gridy >= (abs(target_sizes['y']['max']) + start_y):
      # Hit
      # grid[gridy][gridx] = 'O'
      hitormiss = True
      # print('HIT', highest_y)
      if highest:
        return highest_y
      return start_velocity
    #else:
      # grid[gridy][gridx] = '#'


  return False

def part1():
  highest = 0
  grid_size = (target_sizes['x']['max'] + 1, abs(target_sizes['y']['min']) + 1)

  for x in range(target_sizes['x']['max'] + 1):
    for y in range(-200, 400):
      test = test_velocity((x,y), grid_size, highest=True)
      if test < highest:
        highest = test
  
  print(abs(highest))


def part2():
  hit_velocities = []
  grid_size = (target_sizes['x']['max'] + 1, abs(target_sizes['y']['min']) + 1)

  for x in range(target_sizes['x']['max'] + 1):
    for y in range(-200, 400):
      hit_velocity = test_velocity((x,y), grid_size)
      if hit_velocity:
        hit_velocities.append(hit_velocity)

  print(len(hit_velocities))

part1()
part2()
