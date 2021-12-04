from itertools import *

input = open("01.input").read().splitlines()

def part1():
  prev = None
  increases = 0
  for val in input:
    if prev and int(val) > prev:
      increases += 1
    prev = int(val)
  return increases

def part2():
  prev = None
  increases = 0  
  for idx, val in enumerate(input):
    win = int(input[idx - 2]) + int(input[idx - 1]) + int(val)
    if prev and win > prev:
      increases += 1
    prev = win
  return increases

print(part2())
