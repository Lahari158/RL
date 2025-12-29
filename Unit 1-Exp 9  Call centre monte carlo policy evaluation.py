import random
agents=[0.6,0.8,0.5]

def simulate(policy):
    V=[0,0,0]
    N=[1,1,1]
    for _ in range (1000):
        a=policy(V)
        r=1 if random.random() < agents[a] else 0
        N[a]+=1
        V[a]+=(r-V[a])/N[a]
    return V
random_policy = lambda V: random.randint(0,2)
greedy_policy= lambda V: V.index(max(V))

print("Random Policy:",simulate(random_policy))
print("Greedy Policy:",simulate(greedy_policy))
