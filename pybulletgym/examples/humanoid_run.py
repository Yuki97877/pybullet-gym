import pybullet_envs
import gym
import time

# Humanoid環境の読み込み
env = gym.make("HumanoidFlagrunHarderBulletEnv-v1")
obs = env.reset()

# 10000ステップ分動かす（お好みで増減OK）
for _ in range(10000):
    env.render()  # GUIに表示
    action = env.action_space.sample()  # ランダム行動
    obs, reward, done, info = env.step(action)

    if done:
        obs = env.reset()  # ゴール or 転倒で再スタート

    time.sleep(1.0 / 60.0)  # 60FPSに近づけるためスリープ

env.close()
