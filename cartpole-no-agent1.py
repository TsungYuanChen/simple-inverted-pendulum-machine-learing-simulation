import gymnasium as gym


# 環境を初期化
env = gym.make("CartPole-v1",render_mode="human")

env.reset()
while True:
    # ここにアクションを挿入する。アクションがランダムに生成される。
    action = env.action_space.sample()
    env.render()
    env.step(action)
    

# 環境を終了
env.close()