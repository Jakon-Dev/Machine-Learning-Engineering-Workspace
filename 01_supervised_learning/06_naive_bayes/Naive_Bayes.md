Return to [[Supervised_Learning]]

# Naive Bayes

Naive Bayes is a family of probabilistic classifiers based on Bayes' Theorem, with the "naive" assumption of conditional independence between every pair of features.

## Core Concept
The algorithm calculates the probability of a class given a set of features. Despite its oversimplified assumption, it performs surprisingly well for text classification and high-dimensional datasets.

## Mathematical Intuition
**Bayes' Theorem:**
$$P(y | x_1, \dots, x_n) = \frac{P(y) P(x_1, \dots, x_n | y)}{P(x_1, \dots, x_n)}$$

Using the independence assumption:
$$P(y | x_1, \dots, x_n) \propto P(y) \prod_{i=1}^{n} P(x_i | y)$$

Common variations:
- **Gaussian**: For continuous data (assumes normal distribution).
- **Multinomial**: For discrete counts (e.g., word frequencies).
- **Bernoulli**: For binary features (e.g., word presence/absence).

## Use Cases
- Sentiment analysis.
- Spam filtering.
- Document classification.

## Advantages & Disadvantages
- **Advantages**: Very fast, handles high-dimensional data well, requires little training data.
- **Disadvantages**: The independence assumption is rarely true in real life, can be outperformed by more complex models.

# Quick Challenge
**Objective:** Classify newsgroup posts into different topics using a Multinomial Naive Bayes model.
**Dataset:** `sklearn.datasets.fetch_20newsgroups`
**Evaluation Metric:** Aim for an **F1-Score** of at least **0.75** on a subset of 4 categories (e.g., `sci.med`, `comp.graphics`, `sci.space`, `talk.politics.guns`).
