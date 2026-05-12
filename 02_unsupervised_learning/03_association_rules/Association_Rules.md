Return to [[Unsupervised_Learning]]

# Association Rule Learning

Association rule learning is a rule-based machine learning method for discovering interesting relations between variables in large databases.

## Core Concept
It is primarily used in **Market Basket Analysis** to identify products that are frequently bought together. The most famous example is the "Beer and Diapers" myth.

Rules are usually expressed in the form: $\{ \text{Bread, Butter} \} \Rightarrow \{ \text{Milk} \}$.

## Mathematical Intuition
Three key metrics are used to evaluate rules:
1. **Support**: Frequency of the itemset.
   $$Supp(A \Rightarrow B) = \frac{\text{count}(A \cup B)}{N}$$
2. **Confidence**: Likelihood that item B is bought when item A is bought.
   $$Conf(A \Rightarrow B) = \frac{Supp(A \cup B)}{Supp(A)}$$
3. **Lift**: Ratio of observed support to expected support if A and B were independent.
   $$Lift(A \Rightarrow B) = \frac{Conf(A \Rightarrow B)}{Supp(B)}$$
   (Lift > 1 means A and B are positively associated).

Common algorithms include **Apriori** and **Eclat**.

## Use Cases
- Retail shelf placement.
- E-commerce recommendations ("Customers who bought this also bought...").
- Web usage mining.

## Advantages & Disadvantages
- **Advantages**: Easy to understand, generates actionable business insights.
- **Disadvantages**: Computationally expensive on very large transaction datasets, can generate a massive number of redundant rules.

# Quick Challenge
**Objective:** Discover association rules in a grocery store transaction dataset.
**Dataset:** `Groceries Dataset` (Kaggle or standard UCI repository).
**Evaluation Metric:** Find at least 5 rules with **Lift > 2** and **Confidence > 0.5**.
