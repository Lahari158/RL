import numpy as np

V=np.zeros(5); R=[0,1,0,2,5]; gamma=0.9

for _ in range(50):
    for s in range(5):
        V[s]=R[s]+gamma*max(V[max(s-1,0)],V[min(s+1,4)])
print(V)
