import random

returns=[]
for _ in range(500):
    G=sum(random.choice([1,-1]) for _ in range(10))
    returns.append(G)
print("Value:",sum(returns)/len(returns))
