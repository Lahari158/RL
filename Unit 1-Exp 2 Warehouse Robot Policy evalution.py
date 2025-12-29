import numpy as np
g=4 ; gamma=0.9
items={(1,1)}
goal=(3,3)
obs={(2,2)}
A=[(-1,0),(1,0),(0,-1),(0,1)]
V=np.zeros((g,g))
for _ in range(50):
    Vnew=V.copy()
    for x in range(g):
        for y in range(g):
            v=0
            for a in A:
                nx,ny=x+a[0],y+a[1]
                if not ( 0<=nx<g and 0<=ny<g): continue
                r=5 if (nx,ny)==goal else 2 if (nx,ny) in items else -1 if (nx,ny) in obs else 0
                v+=0.25*(r+gamma*V[nx][ny])
            Vnew[x][y]=v
    V=Vnew
print(np.round(V,2))
            
                
