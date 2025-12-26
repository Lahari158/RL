import numpy as np

V=np.zeros(4); gamma=0.9
R=[0,2,-2,5]   # given rewards
P=0.25         # uniform policy

for _ in range(20):
    for s in range(4):
        V[s]=R[s]+gamma*P*sum(V)
print(V)
