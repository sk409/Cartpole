import gym
import numpy as np

from models import load_model
from model_path import best_path

steps = 200

env = gym.make("CartPole-v0")

model = load_model(best_path)

print("ランダムに行動させる確立を入力してください。(0～100)")
while True:
    epsilon = input()
    if epsilon.isdecimal():
        print("{}%の確率でランダムに行動します。".format(int(epsilon)))
        epsilon = min(100, max(0, int(epsilon)))
        epsilon /= 100
        break
    else:
        print("入力が正しくありません。")

episode = 0
while True:
    obs = env.reset()
    for t in range(steps):
        env.render()
        if np.random.rand() < epsilon:
            action = env.action_space.sample()
        else:
            bs = obs.reshape((1, *obs.shape))
            action = np.argmax(model.predict(obs))
        obs, reward, done, info = env.step(action)
        if done:
            print("Episode-{}: {}steps".format(episode, t))
            break
    episode += 1