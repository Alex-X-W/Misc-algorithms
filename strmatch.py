"""
implements finite automaton of string matching algorithm
"""


class Automaton(object):
  def __init__(self, pattern, string):
    self.pattern = pattern
    self.string = string
    self.states = list(range(len(pattern)))
    self._trans_table = dict()
    self._make_trans()
    self.trans = lambda s, c: self._trans_table[(s, c)]

  def _make_trans(self):
    """ given a state `s` and character `c`, make a transition """
    for s in range(len(self.pattern)+1):
      for c in set(self.pattern + self.string): # traverse the alphabet
        k = min(len(self.pattern), s+1)
        while self.pattern[:k] != (self.pattern[:s]+c)[-k:]:
          k -= 1
          if k == 0:
            break
        self._trans_table[(s, c)] = k

  def match(self):
    s = 0
    m = len(self.pattern)
    for i, c in enumerate(self.string):
      s = self.trans(s, c)
      if s == m:
        print("find occurence at shift {}".format(i-m))

if __name__ == '__main__':
  pattern = 'ti'
  string = 'multinational'
  matcher = Automaton(pattern, string)
  matcher.match()
