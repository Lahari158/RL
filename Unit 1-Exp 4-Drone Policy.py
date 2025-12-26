import numpy as np

V=np.zeros(5); policy=[1]*5; gamma=0.9
R=[0,0,0,1,5]

for _ in range(10):
    for s in range(5):            # policy evaluation
        V[s]=R[s]+gamma*V[min(s+1,4)]
    for s in range(5):            # policy improvement
        policy[s]=np.argmax([V[max(s-1,0)],V[min(s+1,4)]])
print(V,policy)
