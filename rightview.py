"""
given a binary tree, return a list of node values which are on the frontier seen if viewed from the right
"""

from collections import OrderedDict

# build a tree
class Node(object):
  def __init__(self, val=None, left=None, right=None):
    if val:
      self.val = val
      self.left = left
      self.right = right


root = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)


"""
        root
    n2          n3
  n3  n4      n5
        n6      n7
      n8

"""

root.left = n2
root.right = n3
n2.left = n3
n2.right = n4
n3.left = n5
n5.right = n7
n4.right = n6
n6.left = n8


seen = dict()


def rightview(root, d, seen):
  if root:
    rightview(root.right, d+1, seen)
    if d not in seen:
      seen[d] = root.val
    rightview(root.left, d+1, seen)

rightview(root, 0, seen)

ordered_seen = OrderedDict(sorted(seen.items()))

for k, v in ordered_seen.items():
  print("{}: {}".format(k, v))

