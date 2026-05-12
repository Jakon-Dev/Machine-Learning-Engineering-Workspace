Return to [[Supervised_Learning]]

# Linear Regression

Linear Regression is a fundamental supervised learning algorithm used to predict a continuous target variable by modeling the relationship between one or more independent variables (features) and a dependent variable (target).

## Core Concept
The goal of Linear Regression is to find the "best-fit" line (or hyperplane in higher dimensions) that minimizes the vertical distances between the observed data points and the fitted line.

## Mathematical Intuition
The model assumes a linear relationship:
$$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_n x_n + \epsilon$$

Where:
- $y$ is the predicted value.
- $\beta_0$ is the intercept.
- $\beta_1, \dots, \beta_n$ are the coefficients (weights).
- $x_1, \dots, x_n$ are the input features.
- $\epsilon$ is the error term.

To find the optimal coefficients, we minimize the **Mean Squared Error (MSE)**:
$$MSE = \frac{1}{m} \sum_{i=1}^{m} (y_i - \hat{y}_i)^2$$

## Use Cases
- Predicting house prices based on square footage and location.
- Estimating sales revenue based on advertising spend.
- Analyzing the impact of variables on a specific outcome (Inference).

## Advantages & Disadvantages
- **Advantages**: Simple to implement, interpretable, fast to train.
- **Disadvantages**: Assumes linearity, sensitive to outliers, prone to underfitting if the relationship is complex.

# Quick Challenge
**Objective:** Build a Multiple Linear Regression model to predict median house values in California districts.
**Dataset:** `sklearn.datasets.fetch_california_housing`
**Evaluation Metric:** Aim for a **Root Mean Squared Error (RMSE)** of less than **0.7**.
