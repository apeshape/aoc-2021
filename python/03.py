# input = """00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010""".split("\n")

with open("03.input", "r") as f:
    input = [byte.rstrip('\n') for byte in f.readlines()]


def bitcountForPos(pos, list):
  bitsforpos = [bit[pos] for bit in list]
  return [bitsforpos.count("0"), bitsforpos.count("1")]

def getSearchNumber(bc, findMost):
  most = 1 if bc[1] >= bc[0] else 0
  if(findMost):
    return most
  return most ^ 1


def part1(bytes):
  gamma = ""
  epsilon = ""
  bytelen = len(bytes[0])
  for pos in range(0, bytelen):
    bc = bitcountForPos(pos, input)
    most = 0 if bc[0] > bc[1] else 1
    gamma += str(most)
    epsilon += str(most ^ 1)
  
  return int(gamma, base=2) * int(epsilon, base=2)

def part2():
  def getNumber(bytes, most = True, pos = 0):
    if(len(bytes) == 1):
      return bytes[0]
    bc = bitcountForPos(pos, bytes)
    search = getSearchNumber(bc, most)
    filteredBytes = [byte for byte in bytes if byte[pos] == str(search)]
    return getNumber(filteredBytes, most, pos + 1)
  oxy = getNumber(input)
  co2 = getNumber(input, False)

  return int(oxy, base=2) * int(co2, base=2)

print("part1:", part1(input))
print("part2:", part2())