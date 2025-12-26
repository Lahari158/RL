from random import random,betavariate
import math

def run():
    s=f=[1]*3
    for t in range(200):
        a=max(range(3),key=lambda i:betavariate(s[i],f[i]))
        if random()<[0.2,0.4,0.6][a]: s[a]+=1
        else: f[a]+=1
    return s

print(run())
