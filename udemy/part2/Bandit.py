import numpy as np
import matplotlib.pyplot as plt

class Bandit:
    def __init__(self, M):
        self.M = M # True mean
        self.m = 0 # Estimated mean (will update after each iteration)
        self.n = 0 # Current iteration

    def pull(self):
        """ Simulates a pull from the lever, a random number from a dist"""
        return np.random.randn() + self.M # Random from gaussian distr + true mean
        
    def update(self, x):
        """Updates the estimated mean given the value x"""
        self.n += 1
        self.m = (1-1.0/self.n)*self.m + 1/self.n*x # Using formula of new mean

def run_experiment(m1, m2, m3, eps, N):
    bandits = [Bandit(m1), Bandit(m2), Bandit(m3)]
    data = np.empty(N)

    for i in range(N):
        p = np.random.random()
        if p < eps: #Explore
            j = np.random.choice(3)
        else: #Exploit
            j = np.argmax([b.m for b in bandits])

        x = bandits[j].pull()
        bandits[j].update(x)
            
        data[i] = x

    cumulative_average = np.cumsum(data)/ (np.arange(N) + 1)

    plt.plot(cumulative_average) 
    plt.plot(np.ones(N)*m1) # Plots a line y = m1
    plt.plot(np.ones(N)*m2)
    plt.plot(np.ones(N)*m3)
    plt.xscale('log')
    plt.show()

    for b in bandits:
        print(b.m)

    return cumulative_average

c_1 = run_experiment(1.0, 2.0, 3.0, 0.1, 100000)
c_01 = run_experiment(1.0, 2.0, 3.0, 0.01, 100000)
c_3 = run_experiment(1.0, 2.0, 3.0, 0.3, 100000)

plt.plot(c_1, label="eps = 0.1")
plt.plot(c_01, label="eps = 0.01")
plt.plot(c_3, label="eps = 0.3")
plt.show()
