import gym
from datetime import datetime
from gym import wrappers

from agents import DQN
from explorers import LinearDecayEpsilonGreedy, Greedy
from layers import Affine, ReLU, MeanSquaredError
from models import Sequential
from model_path import save_path
from optimizers import Adam
from replay_buffer import ReplayBuffer


num_episodes = 1000
num_steps = 200
success_steps = 100
reward_fail = -1
reward_success = 1
reward_none = 0

env = gym.make("CartPole-v0")
env = wrappers.Monitor(env, "videos", (lambda ep: ep % 100 == 0), True)
num_actions = env.action_space.n
num_observations = env.observation_space.shape[0]

input_shape = (num_observations,)
hidden_size = 32
model = Sequential()
model.add(Affine(hidden_size, input_shape=input_shape))
model.add(ReLU())
model.add(Affine(hidden_size))
model.add(ReLU())
model.add(Affine(hidden_size))
model.add(ReLU())
model.add(Affine(num_actions))
model.compile(MeanSquaredError(), Adam())

explorer = LinearDecayEpsilonGreedy(1.0, 0.0, 500, env.action_space.sample)
replay_buffer = ReplayBuffer(10**6)
agent = DQN(model, replay_buffer, explorer, sync_target_interval=5, replay_size=32, batch_size=8, epochs=2)

print("訓練開始: {}".format(datetime.now().strftime("%Y/%m/%d %H:%M")))
for episode in range(num_episodes):
    obs = env.reset()
    success = False
    for t in range(num_steps):
        env.render()
        agent.train()
        action = agent.act_and_add_experience(obs, reward_none)
        obs, reward, done, info = env.step(action)
        if done:
            print("{}Episode: {}steps".format(episode, t))
            if t >= success_steps:
                success = True
            break
    reward = reward_success if success else reward_fail
    agent.stop_episode_and_train(reward)

print("訓練終了: {}".format(datetime.now().strftime("%Y/%m/%d %H:%M")))
model.save(save_path)