import numpy as np

from collections import deque

class ReplayBuffer:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.clear()


    def __len__(self):
        return self.size

    def clear(self):
        self.observations = deque()
        self.actions = deque()
        self.rewards = deque()
        self.next_observations = deque()

    def add(self, observation, action, reward, next_observation):
        if self.capacity == len(self):
            self.observations.popleft()
            self.actions.popleft()
            self.rewards.popleft()
            self.next_observations.popleft()
        self.observations.append(observation)
        self.actions.append(action)
        self.rewards.append(reward)
        self.next_observations.append(next_observation)
        self.size = min(self.size + 1, self.capacity)


    def sample(self, sample_size):
        assert 0 < sample_size
        sample_size = min(len(self), sample_size)
        indices = np.random.choice(len(self), sample_size, replace=False)
        sample_observations = [self.observations[i] for i in indices]
        sample_actions = [self.actions[i] for i in indices]
        sample_rewards = [self.rewards[i] for i in indices]
        sample_next_observations = [self.next_observations[i] for i in indices]
        return np.array(sample_observations), np.array(sample_actions), np.array(sample_rewards), np.array(sample_next_observations)