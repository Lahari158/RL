import numpy as np

V=np.zeros(5); R=[0,1,0,1,5]; gamma=0.9
for _ in range(20):
    for s in range(5):
        V[s]=R[s]+gamma*(V[s-1] if s>0 else 0)
print("State Values:",V)
