from functools import reduce

with open("10.input", "r") as f:
  input = f.read().split('\n')

def parse_line(line, pairs = {'{':'}','<':'>','(':')','[':']'}, values = {')': 3,']': 57,'}': 1197,'>': 25137}):
  opened = []
  for c in list(line):
    if c in pairs.keys():
      opened.append(c)
    elif c != pairs[opened.pop()]:
      return values[c]
  return [pairs[c] for c in reversed(opened)]
  
def calculate_score(matches):
  return reduce(lambda acc, curr: acc * 5 + curr, [list(')]}>').index(c)+1 for c in matches], 0)

def part2():
  scores = [calculate_score(parse_line(match)) for match in [line for line in input if isinstance(parse_line(line), list)]]
  return sorted(scores)[len(scores) // 2]

print('part1', sum([parse_line(line) for line in input if isinstance(parse_line(line), int)]))
print('part2', part2())