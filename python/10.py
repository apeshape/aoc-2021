import math
from functools import reduce

input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]""".split('\n')

with open("10.input", "r") as f:
  input = f.read().split('\n')

pairs = {'{':'}','<':'>','(':')','[':']'}

def get_invalid_chars(line):
  values = {')': 3,']': 57,'}': 1197,'>': 25137}
  opened = []
  for c in list(line):
    if c in pairs.keys():
      opened.append(c)
    if c in pairs.values():
      closing = opened.pop()
      if c != pairs[closing]:
        return values[c]
  return 0

def get_matches(line):
  opened = []
  for c in list(line):
    if c in pairs.keys():
      opened.append(c)
    if c in pairs.values():
      opened.pop()
  matches = [pairs[c] for c in reversed(opened)]
  return matches

def sum_score(acc, curr):
  acc *= 5
  acc += curr
  return acc

def calculate_score(matches):
  score_table = [')', ']', '}', '>']
  return reduce(sum_score, [score_table.index(c) + 1 for c in matches], 0)

def part1():
  return sum([get_invalid_chars(line) for line in input])

def part2():
  scores = [calculate_score(get_matches(match)) for match in [line for line in input if get_invalid_chars(line) == 0]]
  return sorted(scores)[int(len(scores) / 2)]

print(part1())
print(part2())
