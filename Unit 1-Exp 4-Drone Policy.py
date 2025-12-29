import numpy as np
n,g=5,0.9
goal=(4,4)
A=[(-1,0),(1,0),(0,1),(0,-1)]

V=np.zeros((n,n))
policy=np.zeros((n,n),int)
R= lambda s: 10 if s==goal else -1
for _ in range(20):
    for _ in range(20):
        for x in range (n):
            for y in range(n):
                a=A[policy[x,y]]
                nx,ny=x+a[0],y+a[1]
                if 0<=nx< n and 0<=ny<n:
                    V[x,y]=R((nx,ny))+g*V[nx,ny]
    for x in range (n):
        for y in range (n):
            vals=[]
            for a in A:
                nx,ny=x+a[0],y+a[1]
                if 0<=nx<n and 0<=ny<n:
                    vals.append(R((nx,ny))+g*V[nx,ny])
            policy[x,y]=np.argmax(vals)
print(policy)
        
