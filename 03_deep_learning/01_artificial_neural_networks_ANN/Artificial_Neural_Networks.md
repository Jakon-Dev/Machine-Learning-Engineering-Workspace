Return to [[Deep_Learning]]

# Artificial Neural Networks (ANN)

Artificial Neural Networks, specifically Multilayer Perceptrons (MLP), are the foundation of deep learning. They are inspired by the biological structure of the brain.

## Core Concept
An ANN consists of an input layer, one or more hidden layers, and an output layer. Each layer contains "neurons" connected by weights. Data flows forward through the network (Forward Propagation) to make predictions.

## Mathematical Intuition
Each neuron calculates a weighted sum of its inputs and applies an **Activation Function**:
$$a = f(\sum w_i x_i + b)$$

Common activation functions:
- **ReLU**: $f(z) = \max(0, z)$
- **Sigmoid**: $f(z) = \frac{1}{1 + e^{-z}}$
- **Softmax**: For multiclass output probabilities.

The network learns using **Backpropagation**, which calculates the gradient of the loss function with respect to the weights using the chain rule, and updates weights using **Gradient Descent**:
$$w \leftarrow w - \eta \frac{\partial L}{\partial w}$$

## Use Cases
- Tabular data classification and regression.
- Function approximation.
- Basic pattern recognition.

## Advantages & Disadvantages
- **Advantages**: Universal function approximators, capable of learning non-linear relationships.
- **Disadvantages**: Requires large amounts of data, prone to overfitting (needs regularization), "black box" nature.

# Quick Challenge
**Objective:** Build a Multilayer Perceptron to classify the MNIST handwritten digits.
**Dataset:** `keras.datasets.mnist` or `sklearn.datasets.load_digits`.
**Evaluation Metric:** Aim for a **Test Accuracy** of at least **98%**.
