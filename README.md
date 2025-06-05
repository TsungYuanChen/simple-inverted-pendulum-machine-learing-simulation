# Machine Learning Practice Repository

This repository is built for learning machine learning. It contains three scripts:

1. `no_agent` – runs the simulation without any learning agent.  
2. `learning` – trains a new policy using reinforcement learning.  
3. `load_policy` – loads and runs a pre-trained policy.

The simulation environment used is **Gymnasium**, and the machine learning library is **Stable-Baselines3**.

A trained policy is included in the file `ppo_cartpole_model.zip`. You can use the `load_policy` script to test this pre-trained model.

## Installation

Before running any code, please install the required packages using the following command:

```bash
pip install numpy==1.26 scipy pandas mujoco gymnasium[classic-control] tensorflow stable-baselines3
