from functools import lru_cache
@lru_cache(maxsize=1024)
def ctz(v):
    return (v & -v).bit_length() - 1

@lru_cache(maxsize=4000)
def collatz(n):
    if n == 1:
        return 1
    if n & 1:
        return collatz((n*3+1)//2) + 2
    else:
        return collatz(n>>ctz(n)) + ctz(n)
import math 
@lru_cache(maxsize=8192)
def calc_range(s, e):
    if s >= e:
        return collatz(s)
    if e - s > 1:
        return max(calc_range(s, (s+e)//2), calc_range(math.ceil((s+e+1)/2), e))
    else:
        return max(collatz(s), collatz(e))

import sys

for line in sys.stdin:
    start,end = map(int,line.split())

    m_collatz = 0
    if start > end:
        s,e = end,start
    else:
        s,e = start,end
    
    print(start,end, calc_range(s,e))