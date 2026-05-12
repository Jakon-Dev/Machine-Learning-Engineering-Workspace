Return to [[Supervised_Learning]]

# Logistic Regression

Despite its name, Logistic Regression is a classification algorithm used to predict the probability of a categorical dependent variable. In binary classification, the outcome is usually 0 or 1.

## Core Concept
Logistic Regression uses the **Sigmoid Function** (also known as the Logistic Function) to map any real-valued number into a value between 0 and 1, representing the probability of belonging to a certain class.

## Mathematical Intuition
The probability is calculated as:
$$P(y=1|X) = \sigma(z) = \frac{1}{1 + e^{-z}}$$
Where $z = \beta_0 + \beta_1 x_1 + \dots + \beta_n x_n$.

To train the model, we minimize the **Log Loss** (Cross-Entropy Loss):
$$J(\beta) = -\frac{1}{m} \sum_{i=1}^{m} [y_i \log(\hat{p}_i) + (1 - y_i) \log(1 - \hat{p}_i)]$$

## Use Cases
- Spam detection (Spam vs. Not Spam).
- Medical diagnosis (Disease present vs. Absent).
- Credit scoring (Default vs. No Default).

## Advantages & Disadvantages
- **Advantages**: Outputs probabilities, easy to regularize (L1/L2), efficient.
- **Disadvantages**: Assumes linear decision boundaries, can't solve non-linear problems without feature engineering.

# Quick Challenge
**Objective:** Predict the survival of passengers on the Titanic based on features like age, sex, and class.
**Dataset:** `seaborn.load_dataset('titanic')` (Clean missing values first!)
**Evaluation Metric:** Aim for an **Accuracy** of at least **80%**.
