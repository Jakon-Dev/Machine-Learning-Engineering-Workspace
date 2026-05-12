Return to [[Supervised_Learning]]

# Decision Trees and Random Forests

Decision Trees are non-parametric supervised learning methods used for both classification and regression. Random Forests are an ensemble of many decision trees, typically trained with the "bagging" method.

## Core Concept
- **Decision Trees**: Split the data into subsets based on the most significant attribute at each node. The goal is to maximize the "purity" of the resulting nodes.
- **Random Forests**: Combine multiple trees to reduce variance and improve generalization. Each tree is built on a random subset of the data and features.

## Mathematical Intuition
Splits are determined using metrics like **Gini Impurity** or **Information Gain (Entropy)**.

**Gini Impurity:**
$$G = 1 - \sum_{i=1}^{c} p_i^2$$

**Entropy:**
$$H = -\sum_{i=1}^{c} p_i \log_2(p_i)$$

Random Forests use **Bagging** (Bootstrap Aggregating) to average the results of multiple trees, reducing the risk of overfitting.

## Use Cases
- Fraud detection.
- Customer churn prediction.
- Feature importance analysis.

## Advantages & Disadvantages
- **Advantages**: Easy to visualize, handles both numerical and categorical data, requires little data preprocessing.
- **Disadvantages**: Trees are prone to overfitting (high variance), can be unstable to small variations in data.

# Quick Challenge
**Objective:** Classify breast cancer tumors as malignant or benign.
**Dataset:** `sklearn.datasets.load_breast_cancer`
**Evaluation Metric:** Aim for an **Accuracy** of at least **95%** using a Random Forest Classifier.
