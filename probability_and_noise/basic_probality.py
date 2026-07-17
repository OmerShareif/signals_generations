import numpy as np
import matplotlib.pyplot as plt

def die_roll_experiment(n_rolls=1000):
    outcomes = [1,2,3,4,5,6]
    rolls = np.random.choice(outcomes,size=n_rolls,replace=True)

    # Calculate empirical probabilities
    unique,counts = np.unique(rolls,return_counts=True)
    empirical_probs = counts/n_rolls
    theoritical_probs = np.ones(6)/6

    plt.figure()
    plt.bar(unique,counts,label="Empirical")
    plt.xlabel("Die Face")
    plt.ylabel("Frequency")
    plt.title(f"Die rolls (n={n_rolls})")
    plt.legend()

    plt.figure()
    plt.bar(unique-0.2,empirical_probs,width=0.4,label="Empirical")
    plt.bar(unique+0.2,theoritical_probs,width=0.4,label="Theoritical")
    plt.xlabel("Die face")
    plt.ylabel("Probability")
    plt.title("Probability comparison")
    plt.legend()

    plt.tight_layout()
    plt.show()

    return empirical_probs,theoritical_probs

empirical,theoritical = die_roll_experiment(1000)
print(f"Empirical Probability : {empirical}")
print(f"Theoritical probability : {theoritical}")