from stable_baselines3 import PPO
import gym
import pybullet_envs

# 環境を作成
env = gym.make("HumanoidFlagrunHarderBulletEnv-v0")

# モデル作成（PPOを使用）
model = PPO("MlpPolicy", env, verbose=1)

obs = env.reset()
for _ in range(100000):
    env.render()
    action, _states = model.predict(obs)
    obs, reward, done, info = env.step(action)
    model.learn(total_timesteps=1)  # 1ステップずつ学習
    if done:
        obs = env.reset()


# モデルを保存
model.save("models/humanoid_model")
