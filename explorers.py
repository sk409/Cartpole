import numpy as np

class LinearDecayEpsilonGreedy:

    def __init__(self, start_epsilon, end_epsilon, decay_steps, random_func):
        assert 0 <= start_epsilon <= 1
        assert 0 <= end_epsilon <= 1
        assert end_epsilon <= start_epsilon
        assert decay_steps != 0
        self.start_epsilon = start_epsilon
        self.end_epsilon = end_epsilon
        self.decay_steps = decay_steps
        self.random_func = random_func

    def compute_epsilon(self, t):
        if self.decay_steps <= t:
            return self.end_epsilon
        diff_epsilon = self.end_epsilon - self.start_epsilon
        return self.start_epsilon + diff_epsilon * (t / self.decay_steps)

    def select_action(self, t, obs, greedy_func):
        epsilon = self.compute_epsilon(t)
        if np.random.rand() <= epsilon:
            return self.random_func()
        return greedy_func(obs)


class ConstantEpsilonGreedy:

    def __init__(self, epsilon, random_func):
        assert 0.0 <= epsilon <= 1.0
        self.epsilon = epsilon
        self.random_func = random_func

    def select_action(self, t, obs, greedy_func):
        if np.random.rand() <= self.epsilon:
            return self.random_func()
        return greedy_func(obs)


class Greedy:

    def select_action(self, t, obs, greedy_func):
        return greedy_func(obs)


class Random:

    def __init__(self, random_func):
        self.random_func = random_func

    def select_action(self, t, obs, greedy_func):
        return self.random_func()
