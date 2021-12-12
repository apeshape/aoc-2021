input = """start-A
start-b
A-c
A-b
b-d
A-end
b-end""".split('\n')

# input = """fs-end
# he-DX
# fs-he
# start-DX
# pj-DX
# end-zg
# zg-sl
# zg-pj
# pj-he
# RW-he
# fs-DX
# pj-RW
# zg-RW
# start-pj
# he-WI
# zg-he
# pj-fs
# start-RW""".split('\n')

input = """by-TW
start-TW
fw-end
QZ-end
JH-by
ka-start
ka-by
end-JH
QZ-cv
vg-TI
by-fw
QZ-by
JH-ka
JH-vg
vg-fw
TW-cv
QZ-vg
ka-TW
ka-QZ
JH-fw
vg-hu
cv-start
by-cv
ka-cv""".split('\n')

caves = {}
for line in input:
  cave, connection = line.split('-')
  if not caves.get(cave):
    caves[cave] = []
  caves[cave].append(connection)
  
  if not caves.get(connection):
    caves[connection] = []
  caves[connection].append(cave)
  
def get_duplicate_small(str):
  strcaves = [s for s in str.split(',') if s != 'start' and s != 'end' and s.islower()]
  counts = {c: 0 for c in strcaves if c.islower()}
  for cave in strcaves:
    counts[cave] += 1
  return counts

def next_cave(start, steps, all_paths, test_small):
  if(start == 'end'):
    all_paths.append(steps)
    return all_paths

  to_visit = caves[start]
  for v in to_visit:
    if v != 'start':
      next_step = steps + ',' + v
      if v.isupper():
        next_cave(v, next_step, all_paths, test_small)
      elif test_small(v, steps, next_step):
        next_cave(v, next_step, all_paths, test_small)

def test_part1(v, steps, next_step):
  return next_step.count(v) < 2
def test_part2(v, steps, next_step):
  return next_step.count(v) < 3 and list(get_duplicate_small(steps).values()).count(2) < 2

def part1():
  all_paths = []
  next_cave('start', 'start', all_paths, test_part1)
  return len(all_paths)
  
def part2():
  all_paths = []
  next_cave('start', 'start', all_paths, test_part2)
  return len(all_paths)

print(part1())
print(part2())
# print(len(all_steps))