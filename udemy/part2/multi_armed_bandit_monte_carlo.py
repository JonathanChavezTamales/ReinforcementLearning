import random
import matplotlib.pyplot as plt
import argparse

machines = 3
iterations = 100005
probabilities = (.1, .4, .2)
wins = [0,0,0]
step_probs = [[],[],[]]
step_error = [[],[],[]]


for i in range(iterations):
    
    for j in range(machines):
        ran = random.random()
        if ran < probabilities[j]:
            wins[j] += 1
        res = wins[j]/(i+1)
        step_probs[j].append(res)
        step_error[j].append(abs(res-probabilities[j]))

for i in range(machines):
    print(step_probs[i][-1])

plt.plot(step_probs[0][3:], 'g')
plt.plot(step_probs[1][3:], 'r')
plt.plot(step_probs[2][3:], 'b')
plt.ylabel("calculated mean")
plt.xlabel("iteration")
plt.title("Multi-armed Bandit")
plt.show()
