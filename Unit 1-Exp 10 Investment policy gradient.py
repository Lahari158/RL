import numpy as np

theta=0.0; alpha=0.01
for _ in range(500):
    action=np.random.normal(theta,1)
    reward=action
    theta+=alpha*reward
print("Optimal Policy:",theta)
