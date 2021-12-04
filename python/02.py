instructions = [instruction.split(" ") for instruction in open("02.input", "r").read().splitlines()]

def part1():
  position = {
    "horizontal": 0,
    "depth": 0,
  }
  for direction, value in instructions:
    intval = int(value)
    if direction == "up":
      position["depth"] -= intval
    if direction == "down":
      position["depth"] += intval
    if direction == "forward":
      position["horizontal"] += intval
  
  return position["horizontal"] * position["depth"]

def part2():
  position = {
    "horizontal": 0,
    "depth": 0
  }
  aim = 0
  for direction, value in instructions:
    intval = int(value)
    if direction == "up":
      aim -= intval
    if direction == "down":
      aim += intval
    if direction == "forward":
      position["horizontal"] += intval
      position["depth"] += aim * intval
  return position["horizontal"] * position["depth"]

print(part1())
print(part2())