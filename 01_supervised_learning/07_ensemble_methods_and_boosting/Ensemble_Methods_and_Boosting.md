Return to [[Supervised_Learning]]

# Ensemble Methods and Boosting

Ensemble methods combine multiple base models (weak learners) to create a stronger, more robust model.

## Core Concept
- **Bagging (Bootstrap Aggregating)**: Trains models in parallel on random subsets of data (e.g., Random Forest). Reduces variance.
- **Boosting**: Trains models sequentially, where each new model attempts to correct the errors of the previous ones. Reduces bias.
- **Stacking**: Trains a "meta-model" to combine the predictions of several different base models.

## Mathematical Intuition
**Gradient Boosting**: Minimizes a loss function $L(y, F(x))$ by iteratively adding a new model $h(x)$ that follows the negative gradient of the loss:
$$F_{m}(x) = F_{m-1}(x) + \eta \cdot h_m(x)$$
Where $\eta$ is the learning rate.

Popular implementations include **XGBoost**, **LightGBM**, and **CatBoost**.

## Use Cases
- Winning Kaggle competitions.
- High-stakes classification (credit risk, medical diagnosis).
- Complex regression tasks.

## Advantages & Disadvantages
- **Advantages**: State-of-the-art accuracy, robust to noise, handles non-linear patterns.
- **Disadvantages**: Computationally expensive, hard to interpret ("black box"), sensitive to hyperparameter tuning.

# Quick Challenge
**Objective:** Predict whether a customer will churn using an Gradient Boosting Classifier (or XGBoost).
**Dataset:** `Telco Customer Churn` (can be found on Kaggle or use a similar synthetic dataset).
**Evaluation Metric:** Aim for an **AUC-ROC score** of at least **0.85**.
