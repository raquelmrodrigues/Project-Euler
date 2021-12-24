# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of 
# the numbers from 1 to 20?

from math import gcd
from functools import reduce

for i in range(int(input())):
    N = int(input())
    print(reduce(lambda x,y: x*y//gcd(x,y), range(1,N+1)))