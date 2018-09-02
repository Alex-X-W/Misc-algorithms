"""
an implementation of Knuth-Morris-Pratt string matching algorithm
"""

pattern = 'ti'
string = 'multinational'

# pi: s |-> pi(s), which find the longest suffix of `pattern[:s]` which is also a prefix of `pattern` 
pi_table = dict()
pi_table[0] = 0

# compute pi
s = 1
while s <= len(pattern):
  
  suff_len = s - 1
  while suff_len > 0:
    if pattern[:s][-suff_len:] != pattern[:suff_len]:
      suff_len -= 1
    else:
      break
  pi_table[s] = suff_len
  
  s += 1

pi = lambda s: pi_table[s]

# match
pos = 0
s = 0

while pos < len(string):

  c = string[pos]

  while True:
    if c != pattern[s]:
      s = pi(s)
    else:
      if s == len(pattern) - 1:
        s = pi(s)
        print("find occurence at shift: {}".format(pos))
      s += 1
      break
    if s == 0:
      break

  pos += 1