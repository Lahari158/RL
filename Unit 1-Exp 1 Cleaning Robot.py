import numpy as np

n=5; gamma=0.9
V=np.zeros((n,n))
dirt={(1,2),(3,3)}; obs={(2,2)}

for _ in range(50):
    for i in range(n):
        for j in range(n):
            if (i,j) in obs: continue
            r = 1 if (i,j) in dirt else 0
            V[i,j]=r+gamma*max(
                V[min(i+1,4),j],V[i,max(j-1,0)],
                V[max(i-1,0),j],V[i,min(j+1,4)]
            )
print(V)
