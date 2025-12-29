import numpy as np
n,g=5,0.9
A=[(-1,0),(1,0),(0,-1),(0,1)]
pickup=(4,4)
V=np.zeros((n,n))
policy=np.zeros((n,n),int)
R= lambda s: 10 if s==pickup else -1
for _ in range (50):
    for x in range(n):
        for y in range(n):
            vals=[]
            for a in A:
                nx,ny=x+a[0],y+a[1]
                if 0<=nx<n and 0<=ny<n:
                    vals.append(R((nx,ny))+g*V[nx,ny])
            V[x,y]=max(vals)
            policy[x,y]=np.argmax(vals)
print(V)
print(policy)
