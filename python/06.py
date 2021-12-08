import time
import math

testinput = "3,4,3,1,2"
input = "4,5,3,2,3,3,2,4,2,1,2,4,5,2,2,2,4,1,1,1,5,1,1,2,5,2,1,1,4,4,5,5,1,2,1,1,5,3,5,2,4,3,2,4,5,3,2,1,4,1,3,1,2,4,1,1,4,1,4,2,5,1,4,3,5,2,4,5,4,2,2,5,1,1,2,4,1,4,4,1,1,3,1,2,3,2,5,5,1,1,5,2,4,2,2,4,1,1,1,4,2,2,3,1,2,4,5,4,5,4,2,3,1,4,1,3,1,2,3,3,2,4,3,3,3,1,4,2,3,4,2,1,5,4,2,4,4,3,2,1,5,3,1,4,1,1,5,4,2,4,2,2,4,4,4,1,4,2,4,1,1,3,5,1,5,5,1,3,2,2,3,5,3,1,1,4,4,1,3,3,3,5,1,1,2,5,5,5,2,4,1,5,1,2,1,1,1,4,3,1,5,2,3,1,3,1,4,1,3,5,4,5,1,3,4,2,1,5,1,3,4,5,5,2,1,2,1,1,1,4,3,1,4,2,3,1,3,5,1,4,5,3,1,3,3,2,2,1,5,5,4,3,2,1,5,1,3,1,3,5,1,1,2,1,1,1,5,2,1,1,3,2,1,5,5,5,1,1,5,1,4,1,5,4,2,4,5,2,4,3,2,5,4,1,1,2,4,3,2,1"
allfish = list(map(int, input.split(',')))

def get_all_fish(startfish, days):
  lanterns_for_days = list([0 for i in range(0,9)])

  for seed in startfish:
    lanterns_for_days[int(seed)] += 1

  day = 0
  while day < days:
    # print(day, startfish)
    spawns_today = (day + 7) % 9
    born_at = (day + 1) % 9
    lanterns_for_days[spawns_today] += lanterns_for_days[born_at]
    print("spawns today (%d): %d, with %d new fish" % (day, spawns_today, lanterns_for_days[spawns_today]))

    day += 1

  return lanterns_for_days

aresult = get_all_fish(testinput.split(','), 18)
print(sum(aresult), aresult)

# allfish = [1]

# def get_fish_total(fish, days = 0):
#   cached = {}

#   if(cached.get(fish)):
#     return cached[fish]

#   ellapsed = 0
#   everyfish = [fish]
#   while ellapsed < days:
#     for idx, fish in enumerate(everyfish):
#       if fish == 0:
#         everyfish.append(9)
#         everyfish[idx] = 6
#       else:
#         everyfish[idx] -= 1
#     ellapsed += 1
#   cached[fish] = len(everyfish)
#   return len(everyfish)


# def part1(testdays, fisharray):
#   days = 0
#   while days < testdays:
#     for idx, fish in enumerate(fisharray):
#       if fish == 0:
#         fisharray.append(9)
#         fisharray[idx] = 6
#       else:
#         fisharray[idx] -= 1
#     days += 1
#   return len(fisharray)


# def part2():
#   fishcount = 0
#   for fish in [0]:
#     fc = get_fish_total(fish, 256)
#     fishcount += fc
#     print(fc)

#   print(fishcount)

# def get_total_kids(fish, days, cache = {}):
#   # if cache.get((fish, days)):
#   #   return cache[(fish, days)]

#   if(days - fish <= 0):
#     return 0

#   kids = 0
#   for i in range(0, days - fish):
#     kids += 1 if i % 6 == 0 else 0

#   print("fish %d gets %d kids in %d days, diff: %d" % (fish, kids, days, days - fish))

#   grandkids = 0
#   if(kids > 0):
#     for kid in range(0, kids):
#       f = 6
#       startdays = days - (fish + 2)

#       grandkids += get_total_kids(f, startdays)
#       print("grandkids: %d" % grandkids)
#       # cache[(f, startdays)] = grandkids
#       # sum += grandkids



#   print(grandkids, kids)
#   # return sum + kids
#   return kids + grandkids

# def get_possible_kids(offset, days, cache = {}):
#   diff = days - offset
#   possible_kids = 0

#   # if cache.get(diff):
#   #   return cache[diff]

#   if(diff < 6):
#     return 0

#   for i in range(0, diff):
#     possible_kids += 1 if i % 7 == 0 else 0

#   print("possible kids %d from days %d" % (possible_kids, diff))
#   grandkids = 0
#   if possible_kids > 0:
#     for i in range(1, possible_kids + 1):
#       startday = diff - (8 * i)
#       if startday > 6:
#         grandkids += get_possible_kids(0, startday)
#         # print('kid %d kids from %d. grandkids: %d' % (i, startday, grandkids))
#       # cache[startday] = grandkids
#   return possible_kids + grandkids

# def get_fish(days, fisharr):
#   fishcache = {}
#   asum = 0
#   for fish in fisharr:
#     if(fishcache.get(fish)):
#       asum += fishcache[fish]
#     else:
#       kids = get_possible_kids(fish, days)
#       print(kids)
#       fishcache[fish] = kids
#       asum += kids
#     # print(kids)
#   return asum + len(fisharr)

# print(get_possible_kids(3, 18))



# testdays = 22
# print('better:', get_possible_kids(3, testdays))
# print('better:', get_fish(testdays, allfish))

# def fish(seed, days):
#   daystokids = seed
#   kids = 0
#   while days > 1:
#     if daystokids == 0:
#       print('a kid', daystokids)
#       kids += 1
#       daystokids = 6
#     daystokids -= 1
#     days -= 1
#   return kids

"""
10 -> 12
17 -> 22
18 -> 26
80 -> 5934


18  3   <-
17  2
16  1
15  0   8   <-
14  6   7
13  5   6
12  4   5
11  3   4
10  2   3
9   1   2
8   0   1   8   <-
7   6   0   7   8   <-
6   5   6   6   7
5   4   5   5   6
4   3   4   4   5
3   2   3   3   4
2   1   2   2   3
1   0   1   1   2   8   <-


22  3
21  2
20  1
19  0
18  6
17  5
16  4
15  3
14  2
13  1
12  0
11  6
10  5
9   4
8   3
7   2
6   1
5   0
4   6
3   5
2   4
1   3
0   2


"""



# 14, 13, 12, 11, 11, 10


# start_time = time.time()
# part2()
# print('time:', time.time() - start_time)