
# 强化学习

深度强化学习（DRL，deep reinforcement learning）是深度学习与强化学习相结合的产物，它集成了深度学习在视觉等感知问题上强大的理解能力，以及强化学习的决策能力，实现了端到端学习。深度强化学习的出现使得强化学习技术真正走向实用，得以解决现实场景中的复杂问题。从2013年DQN（深度Q网络，deep Q network）出现到目前为止，深度强化学习领域出现了大量的算法，以及解决实际应用问题的论文.

:::{figure} /_images/deeplearning/drl.png
:align: center
:scale: 70%
:::


:::{warning}
The Policy gradient method are from PG is all you need [^1]! The DQN method are from Rainbow is all you need [^2]! Another useful github repository is apachecn/ailearning [^3].
:::


## Table of contents

:::{toctree}
:maxdepth: 2

Actor-Critic <A2C.ipynb>
Proximal Policy Optimization <PPO.ipynb>
Deep Deterministic Policy Gradient <DDPG.ipynb>
TD3 <TD3.ipynb>
Soft Actor Critic (SAC) <SAC.ipynb>
DDPGfD <DDPGfD.ipynb>
Behavior Cloning (without HER) <BC.ipynb>
Deep Q Network (DQN) <dqn.ipynb>
Double DQN <double_q.ipynb>
Prioritized Experience Replay (PER) <per.ipynb>
Dueling Network <dueling.ipynb>
Noisy Networks for Exploration <noisy_net.ipynb>
Categorical DQN <categorical_dqn.ipynb>
N-Step Learning <n_step_learning.ipynb>
Rainbow <rainbow.ipynb>
:::


[^1]: <https://github.com/MrSyee/pg-is-all-you-need>
[^2]: <https://github.com/Curt-Park/rainbow-is-all-you-need>
[^3]: <https://github.com/apachecn/AiLearning>