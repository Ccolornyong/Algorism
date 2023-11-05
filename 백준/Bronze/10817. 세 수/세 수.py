import sys
import math

a,b,c = map(int, input().split())

ma = max(a,b,c)
mi = min(a,b,c)

mid = (a+b+c)-(ma+mi)
print(mid)