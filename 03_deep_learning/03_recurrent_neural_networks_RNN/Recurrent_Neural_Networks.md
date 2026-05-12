Return to [[Deep_Learning]]

# Recurrent Neural Networks (RNN)

Recurrent Neural Networks are a class of neural networks designed for sequential data, where the order of information matters.

## Core Concept
Unlike feedforward networks, RNNs have connections that loop back, allowing them to maintain a "hidden state" or memory of previous inputs. This makes them ideal for tasks involving time series, text, and speech.

Advanced variants:
- **Long Short-Term Memory (LSTM)**: Solves the vanishing gradient problem by using "gates" to control information flow.
- **Gated Recurrent Unit (GRU)**: A simpler, faster version of LSTM.

## Mathematical Intuition
At each time step $t$, the hidden state $h_t$ is calculated using the current input $x_t$ and the previous hidden state $h_{t-1}$:
$$h_t = \phi(W_h h_{t-1} + W_x x_t + b)$$
Where $\phi$ is an activation function (usually $tanh$).

The output $y_t$ is then:
$$y_t = W_y h_t + b_y$$

In LSTMs, a "cell state" $C_t$ is added to maintain long-term dependencies.

## Use Cases
- Language translation.
- Stock price prediction.
- Sentiment analysis in text.

## Advantages & Disadvantages
- **Advantages**: Handles variable-length sequences, models temporal dependencies.
- **Disadvantages**: Prone to vanishing/exploding gradients, slow to train sequentially.

# Quick Challenge
**Objective:** Predict whether a movie review is positive or negative using an LSTM network.
**Dataset:** `keras.datasets.imdb`
**Evaluation Metric:** Aim for a **Test Accuracy** of at least **85%**.
