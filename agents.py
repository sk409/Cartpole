import copy
import numpy as np


import skml_config

class Random:

    def __init__(self, random_func):
        self.random_func = random_func
    
    def act(self, obs):
        return self.random_func()

class DQN:

    def __init__(
        self,
        q_function,
        replay_buffer,
        explorer,
        gamma = 0.99,
        train_interval=1,
        sync_target_interval=2,
        replay_size=1024,
        batch_size=32,
        epochs = 1
    ):
        assert replay_size <= replay_buffer.capacity
        self.q_function = q_function
        self.replay_buffer = replay_buffer
        self.explorer = explorer
        self.gamma = gamma
        self.train_interval = train_interval
        self.sync_target_interval = sync_target_interval
        self.replay_size = replay_size
        self.batch_size = batch_size
        self.epochs = epochs
        self.t = 0
        self.last_obs = None
        self.last_action = None
        self.target_q_function = q_function
        self.sync_target_q_function()

    def act(self, obs):
        obs = np.reshape(obs, (1, *obs.shape))
        action = np.argmax(self.q_function.predict(obs)[0])
        return action
        # sample_obs, *_ = self.replay_buffer.sample(1)
        # obs = [obs] + [np.array(sample_obs).reshape(-1)]
        # obs = np.array(obs)
        # action = np.argmax(self.q_function.predict(obs, True)[0])
        # return action

    def act_and_add_experience(self, obs, reward):
        if self.last_obs is not None:
            self.replay_buffer.add(self.last_obs, self.last_action, reward, obs)
        action = self.explorer.select_action(self.t, obs, self.act)
        self.last_obs = obs
        self.last_action = action
        return action

    def stop_episode_and_train(self, reward):
        self.replay_buffer.add(self.last_obs, self.last_action, reward, None)
        self.last_obs = None
        self.last_action = None
        self.t += 1
        if self.t % self.train_interval == 0:
            self.train()
        if self.t % self.sync_target_interval == 0:
            self.sync_target_q_function()
            

    def train(self):
        if len(self.replay_buffer) == 0:
            return
        targets = []
        observations, actions, rewards, next_observations = self.replay_buffer.sample(self.replay_size)
        for observation, action, reward, next_observation in zip(observations, actions, rewards, next_observations):
            target = reward
            if next_observation is not None:
                next_observation = np.reshape(next_observation, (1, *next_observation.shape))
                next_action = np.argmax(self.q_function.predict(next_observation)[0])
                target += self.gamma * self.target_q_function.predict(next_observation)[0][next_action]
            observation = np.reshape(observation, (1, *observation.shape))
            targets.append(self.q_function.predict(observation)[0])
            targets[len(targets)-1][action] = target
        self.q_function.fit(observations, np.array(targets), self.batch_size, self.epochs, verbose=-1)

    def sync_target_q_function(self):
        self.target_q_function = copy.deepcopy(self.q_function)
        


        
    
        