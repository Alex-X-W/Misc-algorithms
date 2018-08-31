"""
an implementation of quicksort
"""

def pivot(arr, s, e):
  def swap(arr, l, r):
    buf = arr[l]
    arr[l] = arr[r]
    arr[r] = buf

  pvt = arr[e]
  itr = s
  left = s
  while itr < e:
    if arr[itr] < pvt:
      swap(arr, left, itr)
      left += 1
      itr += 1
    else:
      itr += 1
  swap(arr, left, e)
  return left


def quicksort(arr, s, e):
  if s < e:
    q = pivot(arr, s, e)
    quicksort(arr, s, q-1)
    quicksort(arr, q+1, e)

arr = [1, 5, 9, 4, 0, 4, 2, 6, 8, 9, 7]
print('arr before sort: {}'.format(arr))

quicksort(arr, 3, len(arr)-1)
print('arr after sort: {}'.format(arr))