Return to [[Supervised_Learning]]

# Support Vector Machines (SVM)

Support Vector Machines are powerful supervised learning models used for classification and regression. They are particularly effective in high-dimensional spaces.

## Core Concept
The goal of SVM is to find the **optimal hyperplane** that separates classes with the maximum margin. The data points closest to the hyperplane are called **Support Vectors**.

## Mathematical Intuition
For linearly separable data, we find the hyperplane $w^T x + b = 0$ that maximizes the distance $2/\|w\|$.

For non-linear data, SVM uses the **Kernel Trick** to map features into a higher-dimensional space where a linear separator can be found. Common kernels include:
- **Linear**: $K(x, y) = x^T y$
- **Polynomial**: $K(x, y) = (x^T y + r)^d$
- **Radial Basis Function (RBF)**: $K(x, y) = \exp(-\gamma \|x - y\|^2)$

## Use Cases
- Image recognition.
- Text and hypertext categorization.
- Protein classification.

## Advantages & Disadvantages
- **Advantages**: Effective in high dimensions, memory efficient, versatile (kernels).
- **Disadvantages**: Doesn't provide probability estimates directly, sensitive to feature scaling, slow to train on very large datasets.

# Quick Challenge
**Objective:** Perform multiclass classification on the Iris dataset using an SVM with an RBF kernel.
**Dataset:** `sklearn.datasets.load_iris`
**Evaluation Metric:** Aim for an **Accuracy** of at least **97%**.
