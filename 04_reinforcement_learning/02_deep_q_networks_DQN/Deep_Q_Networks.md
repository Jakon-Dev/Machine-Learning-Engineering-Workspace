Return to [[Reinforcement_Learning]]

# Deep Q-Networks (DQN)

Deep Q-Networks extend Q-Learning by using a Neural Network to approximate the Q-values, allowing it to handle high-dimensional or continuous state spaces.

## Core Concept
In complex environments (like Atari games), a Q-Table is impossible to maintain. DQN uses a Deep Neural Network to predict $Q(s, a)$ for all possible actions given the state $s$ as input.

Two critical techniques made DQN stable:
1. **Experience Replay**: Storing past transitions $(s, a, r, s')$ in a buffer and sampling random batches to train the network, breaking the correlation between consecutive samples.
2. **Fixed Target Network**: Using a separate, slowly-updating network to calculate the target Q-values, preventing the training from oscillating or diverging.

## Mathematical Intuition
The loss function for the Q-Network is the Mean Squared Error between the predicted Q-value and the target Q-value:
$$L = \mathbb{E} [ (R + \gamma \max_{a'} Q_{target}(s', a') - Q_{online}(s, a))^2 ]$$

## Use Cases
- Playing Atari games (human-level performance).
- Complex robotics control.
- Autonomous driving simulations.

## Advantages & Disadvantages
- **Advantages**: Handles continuous and high-dimensional inputs (like pixels), very powerful.
- **Disadvantages**: Hard to tune, unstable training, computationally expensive.

# Quick Challenge
**Objective:** Train an agent to balance a pole on a cart for as long as possible.
**Dataset:** `Gymnasium` `CartPole-v1` environment.
**Evaluation Metric:** Aim for an **Average Reward** of at least **200** (or the maximum of 500) over 100 consecutive episodes.
