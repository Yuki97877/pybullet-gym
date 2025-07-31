from stable_baselines3 import PPO
import gym
import pybullet_envs

# 環境を作成
env = gym.make("HumanoidFlagrunHarderBulletEnv-v0")

# モデル作成（PPOを使用）
model = PPO("MlpPolicy", env, verbose=1)

# 学習
model.learn(total_timesteps=100_000)


# モデルを保存
model.save("models/humanoid_model")
