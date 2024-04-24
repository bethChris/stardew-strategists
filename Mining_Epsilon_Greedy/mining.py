import numpy as np
import matplotlib.pyplot as plt

rock_distribution = {
    "1-19": {"Copper": 1.0, "Iron": 0.0, "Gold": 0.0},
    "21-39": {"Copper": 0.9, "Iron": 0.1, "Gold": 0.0},
    "41-59": {"Copper": 0.25, "Iron": 0.75, "Gold": 0.0},
    "61-79": {"Copper": 0.225, "Iron": 0.675, "Gold": 0.1},
    "81-119": {"Copper": 0.0625, "Iron": 0.1875, "Gold": 0.75}
}

rock_values = {"Copper": 1, "Iron": 2, "Gold": 3}

def get_probabilities():
    probs = []
    for level, rocks in rock_distribution.items():
        prob = sum(value for value in rocks.values() if value is not None)
        probs.append(prob)
    return probs


def choose_action(actions, epsilon):
    num_actions = len(actions)
    p = np.random.random()
    if p < epsilon:
        j = np.random.choice(num_actions)
    else:
        j = np.argmax([a['runningMean'] for a in actions])
    x = np.random.randn() + actions[j]['mean']
    actions[j]['numTimesChosen'] += 1
    actions[j]['runningMean'] = (1 - 1.0 / actions[j]['numTimesChosen']) * actions[j]['runningMean'] + 1.0 / \
                                actions[j]['numTimesChosen'] * x
    return j


def run_epsilon_greedy(epsilon, numOfSteps, probabilities, num_simulations):
    cumulative_values = np.zeros(numOfSteps)

    for _ in range(num_simulations):
        actions = [{'mean': prob, 'runningMean': 0, 'numTimesChosen': 0} for prob in probabilities]
        values = np.zeros(numOfSteps)

        for i in range(numOfSteps):
            chosen_index = choose_action(actions, epsilon)
            chosen_level = list(rock_distribution.keys())[chosen_index]
            rocks = rock_distribution[chosen_level]
            value = sum(rock_values[rock_type] for rock_type, prob in rocks.items() if prob is not None)
            actions[chosen_index]['numTimesChosen'] += 1
            actions[chosen_index]['runningMean'] = (1 - 1.0 / actions[chosen_index]['numTimesChosen']) * \
                                                   actions[chosen_index]['runningMean'] + 1.0 / \
                                                   actions[chosen_index]['numTimesChosen'] * value
            values[i] = actions[chosen_index]['runningMean']

        cumulative_values += np.cumsum(values) / (np.arange(numOfSteps) + 1)

    return cumulative_values / num_simulations


if __name__ == '__main__':
    probabilities = get_probabilities()

    epsilons = [0.01, 0.05, 0.1, 0.4]
    num_simulations = 1

    for epsilon in epsilons:
        result = run_epsilon_greedy(epsilon, 2000, probabilities, num_simulations)
        plt.plot(result, label=f'Epsilon-Greedy (eps={epsilon})')

    plt.legend()
    plt.xlabel('Time Steps')
    plt.ylabel('Average Reward')
    plt.title('Epsilon-Greedy Convergence Rate')
    plt.show()