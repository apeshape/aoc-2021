# input = """NNCB

# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C"""

input = """PPFCHPFNCKOKOSBVCFPP

VC -> N
SC -> H
CK -> P
OK -> O
KV -> O
HS -> B
OH -> O
VN -> F
FS -> S
ON -> B
OS -> H
PC -> B
BP -> O
OO -> N
BF -> K
CN -> B
FK -> F
NP -> K
KK -> H
CB -> S
CV -> K
VS -> F
SF -> N
KB -> H
KN -> F
CP -> V
BO -> N
SS -> O
HF -> H
NN -> F
PP -> O
VP -> H
BB -> K
VB -> N
OF -> N
SH -> S
PO -> F
OC -> S
NS -> C
FH -> N
FP -> C
SO -> P
VK -> C
HP -> O
PV -> S
HN -> K
NB -> C
NV -> K
NK -> B
FN -> C
VV -> N
BN -> N
BH -> S
FO -> V
PK -> N
PS -> O
CO -> K
NO -> K
SV -> C
KO -> V
HC -> B
BC -> N
PB -> C
SK -> S
FV -> K
HO -> O
CF -> O
HB -> P
SP -> N
VH -> P
NC -> K
KC -> B
OV -> P
BK -> F
FB -> F
FF -> V
CS -> F
CC -> H
SB -> C
VO -> V
VF -> O
KP -> N
HV -> H
PF -> H
KH -> P
KS -> S
BS -> H
PH -> S
SN -> K
HK -> P
FC -> N
PN -> S
HH -> N
OB -> P
BV -> S
KF -> N
OP -> H
NF -> V
CH -> K
NH -> P"""


template, instructions_str = input.split('\n\n')
instructions = instructions_str.split('\n')
instructions_dict = {instr.split(' -> ')[0]:instr.split(' -> ')[1] for instr in instructions}
pair_count = {k:0 for k,v in instructions_dict.items()}

def get_template_pairs(tmpl):
  pairs = []
  for idx, element in enumerate(tmpl):
    if idx < len(tmpl) - 1:
      pairs.append(element + tmpl[idx + 1])
  return pairs

tmpl2 = template
for pair in get_template_pairs(tmpl2):
  pair_count[pair] += 1


def print_pc(pair_count):
  for k,v in pair_count.items():
    if v > 0:
      print(k, v)

def get_paircount(prev_pc):
  pc = {k:0 for k,v in instructions_dict.items()}
  
  letters = set(instructions_dict.values())
  letter_count = {k:0 for k in letters}

  for p,c in prev_pc.items():
    pc[p[0] + instructions_dict[p]] += c
    pc[instructions_dict[p] + p[1]] += c
    letter_count[instructions_dict[p]] = c
  return pc

pc = pair_count.copy()
for _ in range(10):
  pc = get_paircount(pc)

def get_letter_count_in_pc(pc):
  letters = set(instructions_dict.values())
  count = {k:0 for k in letters}
  for p, c in pc.items():
    for l in letters:
      if p[0] == l:
        count[l] += c
  return count

print_pc(pc)
lc = get_letter_count_in_pc(pc)
lc[template[-1]] += 1

print(max(lc.values()) - min(lc.values()))