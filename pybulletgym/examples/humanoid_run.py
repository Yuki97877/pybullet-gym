import pybullet_envs
import gym
import time
from stable_baselines3 import PPO

# Humanoid環境の読み込み
env = gym.make("HumanoidFlagrunHarderBulletEnv-v0")
obs = env.reset()

# 学習済みモデルの読み込み
model = PPO.load("models/humanoid_model")

# 10000ステップ分動かす（お好みで増減OK）
for _ in range(10000):
    env.render()  # GUIに表示
    action = env.action_space.sample()  # ランダム行動
    obs, reward, done, info = env.step(action)

    if done:
        obs = env.reset()  # ゴール or 転倒で再スタート

    time.sleep(1.0 / 60.0)  # 60FPSに近づけるためスリープ

env.close()
