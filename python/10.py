import math

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

pairs = {
  '{': '}',
  '<': '>',
  '(': ')',
  '[': ']'
}

def get_invalid_chars(line):

  values = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
  }

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

  opened.reverse()
  matches = [pairs[c] for c in opened]
  return matches

def calculate_score(matches):
  score_table = [')', ']', '}', '>']
  total = 0
  scores = [score_table.index(c) + 1 for c in matches]
  for s in scores:
    total *= 5
    total += s
  
  return total

def part1():
  sum = 0
  for line in input:
    sum += get_invalid_chars(line)
  return sum

def part2():
  incomplete = [line for line in input if get_invalid_chars(line) == 0]
  scores = []
  for tocomplete in incomplete:
    matches = get_matches(tocomplete)
    scores.append(calculate_score(matches))

  return sorted(scores)[int(len(scores) / 2)]

print(part1())
print(part2())
