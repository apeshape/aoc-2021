import math
import json
input = "8A004A801A8002F478"
input = "D2FE28"
input = "38006F45291200"
input = "EE00D40C823060"
input = "620080001611562C8802118E34"
input = "C0015000016115A2E0802F182340"
input = "A0016C880162017C3686B18A3D4780"
input = "C200B40A82"
input = "9C0141080250320F1802104A08"
input = "6053231004C12DC26D00526BEE728D2C013AC7795ACA756F93B524D8000AAC8FF80B3A7A4016F6802D35C7C94C8AC97AD81D30024C00D1003C80AD050029C00E20240580853401E98C00D50038400D401518C00C7003880376300290023000060D800D09B9D03E7F546930052C016000422234208CC000854778CF0EA7C9C802ACE005FE4EBE1B99EA4C8A2A804D26730E25AA8B23CBDE7C855808057C9C87718DFEED9A008880391520BC280004260C44C8E460086802600087C548430A4401B8C91AE3749CF9CEFF0A8C0041498F180532A9728813A012261367931FF43E9040191F002A539D7A9CEBFCF7B3DE36CA56BC506005EE6393A0ACAA990030B3E29348734BC200D980390960BC723007614C618DC600D4268AD168C0268ED2CB72E09341040181D802B285937A739ACCEFFE9F4B6D30802DC94803D80292B5389DFEB2A440081CE0FCE951005AD800D04BF26B32FC9AFCF8D280592D65B9CE67DCEF20C530E13B7F67F8FB140D200E6673BA45C0086262FBB084F5BF381918017221E402474EF86280333100622FC37844200DC6A8950650005C8273133A300465A7AEC08B00103925392575007E63310592EA747830052801C99C9CB215397F3ACF97CFE41C802DBD004244C67B189E3BC4584E2013C1F91B0BCD60AA1690060360094F6A70B7FC7D34A52CBAE011CB6A17509F8DF61F3B4ED46A683E6BD258100667EA4B1A6211006AD367D600ACBD61FD10CBD61FD129003D9600B4608C931D54700AA6E2932D3CBB45399A49E66E641274AE4040039B8BD2C933137F95A4A76CFBAE122704026E700662200D4358530D4401F8AD0722DCEC3124E92B639CC5AF413300700010D8F30FE1B80021506A33C3F1007A314348DC0002EC4D9CF36280213938F648925BDE134803CB9BD6BF3BFD83C0149E859EA6614A8C"

def get_binary_str(hex):
  binary = ''
  for c in hex:
    binary += format(int(c, 16), "04b")

  return binary

def bintodec(bin):
  return int(bin, base=2)

def split_by_len(str, maxlen):
  return [''.join(part) for part in zip(* ([iter(str)] * maxlen))]

def get_literal_value(bin):
  value = ''
  allbits = ''
  for idx, b in enumerate(range(len(bin) // 5)):
    binval = bin[idx * 5: idx * 5 + 5]
    value += binval[1:]
    allbits += binval
    if binval[0] == '0':
      break

  return bintodec(value), allbits

def get_packet(bits):
  version = bintodec(bits[:3])
  type = bintodec(bits[3:6])
  packet = {
    'version': version,
    'type': type,
    'value': 0,
    'children': [],
    'length': 0
  }
  if type == 4:
    value, lit_bits = get_literal_value(bits[6:])
    packet['value'] = value
    packet['length'] += len(lit_bits) + 6
  else:
    itype = bits[6]
    subpacket_num_seg_length = 15 if itype == "0" else 11

    subpackets_len_bits = bits[7: 7 + subpacket_num_seg_length]
    subpackets_len = bintodec(subpackets_len_bits)
    packet['subpackets_len'] = subpackets_len
    packet['i'] = bintodec(bits[6])

    sub_packet_bits = bits[7 + subpacket_num_seg_length:]
    
    packet['length'] += 7 + len(subpackets_len_bits)
    all_subpackets = []

    if packet['i'] == 1:
      subpackets_start = 0
      while len(all_subpackets) < subpackets_len:
        subpacket = get_packet(sub_packet_bits[subpackets_start:])
        packet['length'] += subpacket['length']
        subpackets_start += subpacket['length']
        all_subpackets.append(subpacket)

    else:
      subpackets_start = 0
      while subpackets_start < subpackets_len:
        subpacket = get_packet(sub_packet_bits[subpackets_start:])
        packet['length'] += subpacket['length']
        subpackets_start += subpacket['length']
        all_subpackets.append(subpacket)
    packet['children'] = all_subpackets


  return packet


def sum_versions(packet, sum = 0):
  sum += packet['version']
  for p in packet['children']:
    sum += sum_versions(p)
  
  return sum

def get_packet_sum(packet, total = 0):
  if packet['type'] == 4:
    return packet['value']
  child_values = []
  # print('pack',json.dumps(packet, indent=2))
  for p in packet['children']:
    child_values.append(get_packet_sum(p))

  if packet['type'] == 0:
    return sum(child_values)
  if packet['type'] == 1:
    return math.prod(child_values)
  if packet['type'] == 2:
    return min(child_values)
  if packet['type'] == 3:
    return max(child_values)
  if packet['type'] == 5:
    return 1 if child_values[0] > child_values[1] else 0
  if packet['type'] == 6:
    return 1 if child_values[0] < child_values[1] else 0
  if packet['type'] == 7:
    return 1 if child_values[0] == child_values[1] else 0

  
  print(child_values)
  return total


binary = get_binary_str(input)
print(binary)
p = get_packet(binary)

print(json.dumps(p, indent=2))
# print(sum_versions(p))
print(get_packet_sum(p))


"""
110100101111111000101000
00111000000000000110111101000101001010010001001000000000

38006F45291200
00111000000000000110111101000101001010010001001000000000
VVVTTTILLLLLLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBBBBBB

00111000000000000110111101000101001010010001001000000000
"""