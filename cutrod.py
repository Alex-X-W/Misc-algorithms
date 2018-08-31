"""
a DP rod cutting implementation
"""
import numpy as np

rod_prices = {
  1: 1,
  2: 5,
  3: 8,
  4: 9,
  5: 10,
  6: 17,
  7: 17,
  8: 20,
  9: 24,
  10: 30
}

def opt_price(l, rod_prices):
  if l in rod_prices:
    raw_price = rod_prices[l]
  else:
    raw_price = -np.inf
  
  ret = raw_price
  for i in range(1, l//2):
    ret = max(opt_price(i, rod_prices) + opt_price(l-i, rod_prices), ret)

  return ret

if __name__ == "__main__":
  for i in range(1, 15):
    print("%d    %d" % (i, opt_price(i, rod_prices)))