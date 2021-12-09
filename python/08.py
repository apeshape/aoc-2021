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

def matches_all(test, sample):
  return len(set(test).intersection(sample)) == len(test)

def get_decoder(samples):
  decoded = {
    1: [sample for sample in samples if len(sample) == 2][0],
    4: [sample for sample in samples if len(sample) == 4][0],
    7: [sample for sample in samples if len(sample) == 3][0],
    8: [sample for sample in samples if len(sample) == 7][0],
  }

  decoded[6] = [sample for sample in samples if len(sample) == 6 and len(set(decoded[1]).intersection(sample)) < 2][0]
  decoded[3] = [sample for sample in samples if len(sample) == 5 and len(set(decoded[1]).intersection(sample)) == 2][0]
  decoded[9] = [sample for sample in samples if len(sample) == 6 and len(set(decoded[3]).intersection(sample)) == 5][0]
  decoded[0] = [sample for sample in samples if len(sample) == 6 and sample != decoded[9] and sample != decoded[6]][0]
  decoded[5] = [sample for sample in samples if len(sample) == 5 and len(set(decoded[6]).intersection(sample)) == 5][0]
  decoded[2] = [sample for sample in samples if len(sample) == 5 and len(set(decoded[6]).intersection(sample)) == 4 and len(set(decoded[4]).intersection(sample)) == 2][0]

  return {''.join(sorted(v)): k for k, v in decoded.items()}

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
    decoder = get_decoder(patternsline.split())
    
    out = ""
    for output in outputline.split():
      out += str(decoder[''.join(sorted(output))])
    total += int(out)

  return total


print(part1())
print(part2())