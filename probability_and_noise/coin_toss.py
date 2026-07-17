import numpy as np

#simulate 10000 coin tosses
N = 10000
toss = np.random.choice(['H','T'],size=N)

P_H = np.sum(toss == 'H')/N

print("probability of getting Head:",P_H)