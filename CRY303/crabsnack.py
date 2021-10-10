import math
import random
from decimal import *

from Crypto.Util.number import bytes_to_long

from flag import flag

# first prime numbers
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
          41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# [6:9] may be better but I would like to make it more challenging
seed = bytes_to_long(flag[5:9])
random.seed(seed)
random.shuffle(primes)

# Use ln function
getcontext().prec = 100
keys = []
for i in range(len(flag)):
    keys.append(Decimal(primes[i]).ln())

sum_ = Decimal(0.0)
for i, c in enumerate(flag):
    sum_ += c * Decimal(keys[i])

final = math.floor(sum_ * 2 ** 256)
print(final)
# 595880127300380678523256691710477534988010995960362123959020640388069230984429515
