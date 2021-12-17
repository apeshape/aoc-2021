def get_colored(n):
  if n == 0:
    return '\033[1;31m ' + str(n)
  return '\033[1;32m ' + str(n)

def print_grid(grid, clear=True):
  if clear:
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
  for line in grid:
    strline = [get_colored(n) for n in line]
    print(''.join(strline))
  
  print('-' * len(grid[0]))