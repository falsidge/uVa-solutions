from cmath import sqrt
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
lim = 1000000
inc = int(math.sqrt(lim))
# blocks = [0]*math.ceil(math.sqrt(lim))
# for i in range(1,lim,inc):
#     blocks[(i-1)//inc] = calc_range(i,min(i+inc-1,lim))
    # print(i,min(i+inc-1,lim))
@lru_cache(maxsize=8192)
def calc_block(block):
    return calc_range(block*inc+1,min((block*inc+inc),lim))
for line in sys.stdin:
    start,end = map(int,line.split())

    m_collatz = 0
    if start > end:
        s,e = end,start
    else:
        s,e = start,end
    s = max(s, 1)
    e = min(e, lim)
    block_s = (s-1) // inc
    block_e = (e-1) // inc
    m = 0
    c_block = block_s
    if block_s == block_e:
        m = calc_range(s,e)
    else:
        if s - block_s * inc - 1 > 0:
            m = calc_range(s,block_s*inc+inc)
            # print( m, s, block_s*inc+inc)
            c_block = block_s + 1
        for block in range(c_block, block_e):
            # print(block)
            m = max(m, calc_block(block))
        # print(m)
        if e - block_e * inc - 1 > 0:
            m = max(m, calc_range(block_e*inc+1,e))

    print(start,end, m)