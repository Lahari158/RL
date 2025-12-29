import random
p=(0,0)
d={(1,2),(2,3)}
o={(1,1)}
for i in range(20):
    a=random.choice([(1,0),(-1,0),(0,1),(0,-1)])
    n=(p[0]+a[0],p[1]+a[1])
    if 0<=n[0]<5 and 0<=n[1]< 5:
        p=n
        r=1 if p in d else -1 if p in o else 0
    else:r=-0.2
    print(p,r)
    if p in d:d.remove(p)
    if not d:break
