
import gymnasium as gym
from stable_baselines3 import PPO

# 環境を初期化
env = gym.make("CartPole-v1", render_mode="human")

model = PPO("MlpPolicy", env, verbose=1, tensorboard_log="./logsPPO")
model.learn(total_timesteps=1000000)

# モデルを保存
model.save("ppo_cartpole_model")

state, _ = env.reset()

for _ in range(2000):
    env.render()
    action, _ = model.predict(state, deterministic=True)
    state, reward, terminated, truncated, info = env.step(action)
    
    if terminated or truncated:
       state, _ = env.reset()
      
# 環境を終了
env.close()
