Return to [[Reinforcement_Learning]]

# Q-Learning

Q-Learning is a model-free, off-policy reinforcement learning algorithm used to find the best action to take given a current state.

## Core Concept
An **Agent** interacts with an **Environment** by taking **Actions**. For each action, the agent receives a **Reward** and moves to a new **State**. The goal is to learn a **Policy** that maximizes the total cumulative reward.

Q-Learning maintains a **Q-Table** where each entry $Q(s, a)$ represents the expected future reward of taking action $a$ in state $s$.

## Mathematical Intuition
The Q-values are updated using the **Bellman Equation**:
$$Q(s, a) \leftarrow Q(s, a) + \alpha [R + \gamma \max_{a'} Q(s', a') - Q(s, a)]$$

Where:
- $\alpha$: Learning rate.
- $\gamma$: Discount factor (importance of future rewards).
- $R$: Immediate reward.
- $\max_{a'} Q(s', a')$: Estimated maximum future reward from the next state.

To balance exploring new actions and exploiting known good ones, agents usually use an **$\epsilon$-greedy policy**.

## Use Cases
- Solving grid-world puzzles.
- Simple game AI (e.g., Tic-Tac-Toe).
- Pathfinding in robotics.

## Advantages & Disadvantages
- **Advantages**: Guaranteed to converge to the optimal policy in finite MDPs, no model of the environment required.
- **Disadvantages**: Fails in continuous or large state spaces (due to the Q-Table's size), slow to converge.

# Quick Challenge
**Objective:** Train an agent to navigate the Frozen Lake environment without falling into holes.
**Dataset:** `Gymnasium` (formerly OpenAI Gym) `FrozenLake-v1` environment.
**Evaluation Metric:** Aim for a **Success Rate** (average reward) of at least **0.7** over 100 episodes.
