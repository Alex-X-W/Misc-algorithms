'''
implements different shortest path algorithms, single source and all pairs
'''
import heapq
from numpy import inf


class Node(object):
  def __init__(self, d, p, n): # `d` is the node distance to the source, `p` is the parent
    self.d = d
    self.p = p
    self.name = n

  def add_edges(self, edges):
    self._edges = dict()
    for e in edges:
      self._edges[(e.s, e.t)] = e.w

  @property
  def edges(self):
    return self._edges

  def __repr__(self):
    return self.name

  # overload operator to support python `heapq` heap implementation
  def __gt__(self, other):
    return self.d > other.d

  # overload operator to support python `heapq` heap implementation
  def __lt__(self, other):
    return self.d < other.d


class Edge(object):
  def __init__(self, s, t, w): # `s` is the edge source, `t` is the edge target, 'w' is the edge weight
    self.s = s
    self.t = t
    self.w = w


class Graph(object):
  def __init__(self, nodes):
    self._nodes = nodes
    self._edges = dict()
    for n in nodes:
      self._edges.update(n.edges)

  @property
  def N(self):
    return self._nodes

  @property
  def E(self):
    return self._edges

  def adj(self, node):
    ret = []
    for e in self._edges:
      if e[0] == node:
        ret.append(e[1])
    return ret

  def w(self, u, v):
    return u.edges[(u, v)] if (u, v) in u.edges else inf

  def relax(self, u, v):
    if v.d > u.d + self.w(u, v):
      v.d = u.d + self.w(u, v)
      v.p = u
  

# a graph instance as per p.659 Cormen *Introduction to algorithms*

s = Node(0, None, 's')
t = Node(10, s, 't')
x = Node(inf, None, 'x')
y = Node(5, s, 'y')
z = Node(inf, None, 'z')

s.add_edges([Edge(s, t, 10), Edge(s, y, 5)])
t.add_edges([Edge(t, y, 2), Edge(t, x, 1)])
x.add_edges([Edge(x, z, 4)])
y.add_edges([Edge(y, t, 3), Edge(y, x, 9), Edge(y, z, 2)])
z.add_edges([Edge(z, s, 7), Edge(z, x, 6)])

G = Graph([s, t, x, y, z])


############################### single source

#######
# Bellman-Ford
#######

def Bellman_Ford(G):
  for i in range(len(G.N) - 1):
    for e in G.E:
      G.relax(*e)
  for e in G.E:
    if e[1].d > e[0].d + G.w(*e):
      return False
  return True

# test
test_Bellman_Ford = False

if test_Bellman_Ford:
  if Bellman_Ford(G):
    targets = [t, x, y, z]
    for t in targets:
      print("the shortest path to node {} is of length {}, parented at node {}".format(t, t.d, t.p))


#######
# Dijkstra
#######

def Dijkstra(G):
  Q = G.N.copy()
  heapq.heapify(Q)
  while Q:
    u = heapq.heappop(Q)
    for v in G.adj(u):
      G.relax(u, v)

test_Dijkstra = False
if test_Dijkstra:
  Dijkstra(G)
  targets = [t, x, y, z]
  for t in targets:
    print("the shortest path to node {} is of length {}, parented at node {}".format(t, t.d, t.p))



############################### all pairs

#######
# Dynamic Programming, aka Floyd-Warshall
#######
shortest_path = dict()


def DP(G, opt_path):
  for inter_node in G.N:
    for src in G.N:
      for tgt in G.N:
        if tgt != src:
          if (src, tgt) not in opt_path:
            opt_path[(src, tgt)] = G.E[(src, tgt)] if (src, tgt) in G.E else inf
          elif inter_node != src and inter_node != tgt:
            opt_path[(src, tgt)] = min(opt_path[(src, tgt)], opt_path[(src, inter_node)] + opt_path[(inter_node, tgt)])

test_DP = True
if test_DP:
  DP(G, shortest_path)
  targets = [t, x, y, z]
  for t in targets:
    print("the shortest path to node {} is of length {}".format(t, shortest_path[(s, t)]))


