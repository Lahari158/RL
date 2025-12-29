import random,math
def bandit(strategy):
    Q=[0]*3
    N=[1]*3
    total=0
    for t in range(1,200):
        if strategy=="eps":
            a=random.randint(0,2) if random.random()<0.1 else Q.index(max(Q))
        elif strategy=="ucb":
            a=max(range(3),key=lambda i:Q[i]+math.sqrt(2*math.log(t)/N[i]))
        else:
            a=max(range(3),key= lambda i: random.betavariate(Q[i]+1,N[i]-Q[i]+1))
        r=5 if random.random()< [0.3,0.5,0.7][a] else 0
        N[a]+=1
        Q[a]+=(r-Q[a])/N[a]
        total+=r
    return total
print(bandit("eps"),bandit("ucb"),bandit("tc"))
