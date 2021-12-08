# input = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
# edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
# fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
# fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
# aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
# fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
# dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
# bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
# egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
# gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce""".split('\n')

with open("08.input", "r") as f:
  input = f.read().split('\n')

segcount = {
  'tt': 8,
  'tl': 6,
  'tr': 8,
  'm': 7,
  'bl': 4,
  'br': 9,
  'bb': 7
}

def matches_all(test, sample):
  return len(set(test).intersection(sample)) == len(test)

def get_decoder(samples):
  decoded = {}
  samples_done = []
  numberstypes = {
    7: [8],
    6: [0, 6, 9],
    5: [2, 3, 5],
    4: [4],
    3: [7],
    2: [1]
  }

  while len(samples_done) < 10:
    for sample in [s for s in samples if s not in samples_done]:
      if sample in samples_done:
        continue
      numtypes = numberstypes[len(sample)]

      if(len(numtypes) == 1):
        decoded[numtypes[0]] = sample
        samples_done.append(sample)
    
    for sample in [s for s in samples if s not in samples_done]:
      if sample in samples_done:
        continue

      #  get [0, 6, 9],
      if len(sample) == 6:
        if len(set(decoded[1]).intersection(sample)) < 2:
          decoded[6] = sample
          samples_done.append(sample)
          continue
        if 3 in decoded.keys():
          if len(set(decoded[3]).intersection(sample)) == 5:
            decoded[9] = sample
            samples_done.append(sample)
            continue
          if len(set(decoded[3]).intersection(sample)) == 4:
            decoded[0] = sample
            samples_done.append(sample)
            continue
      # get [2, 3, 5],
      if len(sample) == 5:
        if len(set(decoded[1]).intersection(sample)) == 2:
          decoded[3] = sample
          samples_done.append(sample)
          continue
        if 6 in decoded.keys():
          if len(set(decoded[6]).intersection(sample)) == 5:
            decoded[5] = sample
            samples_done.append(sample)
            continue
          if len(set(decoded[6]).intersection(sample)) == 4:
            decoded[2] = sample
            samples_done.append(sample)
            continue
  return decoded

def get_segments(samples):
  counts = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0,
    'g': 0
  }

  segments = {}
  for sample in samples:
    for c in list(sample):
      counts[c] += 1
  
  decoded_samples = get_decoder(samples)

  for key, count in counts.items():
    if count == 4:
      segments['bl'] = key
    if count == 6:
      segments['tl'] = key
    if count == 9:
      segments['br'] = key
    if count == 8:
      if key in decoded_samples[4]:
        segments['tr'] = key
      else:
        segments['tt'] = key
    if count == 7:
      if key in decoded_samples[0]:
        segments['bb'] = key
      else:
        segments['m'] = key
    
  return segments

bytes = ['1110111', '0010010', '1011101', '1011011', '0111010', '1101011', '1101111', '1010010', '1111111', '1111011']
segkeys = ['tt', 'tl', 'tr', 'm', 'bl', 'br', 'bb']

def get_numbers_with_segments(numstr, segments):
  mask = ''
  for segkey in segkeys:
    mask += segments[segkey]

  byte = list('0000000')
  for idx, m in enumerate(mask):
    if(m in numstr):
      byte[idx] = "1"


  num = bytes.index("".join(byte))
  return str(num)

def part1():
  count = 0

  for line in input:
    patternsline, outputline = line.split(' | ')
    patterns = patternsline.split()
    output = outputline.split()
    
    for num in output:
      if len(num) in [7, 4, 2, 3]:
        count += 1
  return count

def part2():
  total = 0
  for line in input:
    patternsline, outputline = line.split(' | ')

    s = get_segments(patternsline.split())
    out = ""
    for output in outputline.split():
      out += get_numbers_with_segments(output, s)
    # print('out:', out)
    total += int(out)

  return total

print(part1())
print(part2())