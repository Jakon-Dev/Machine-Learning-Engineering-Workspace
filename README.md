# Machine Learning Engineering Workspace

A structured learning journey through the world of Machine Learning, designed for a Computer Engineer. This repository serves as a workspace to practice, implement, and document ML algorithms and projects from the ground up.

## Strict Disclaimer
This project is a personal learning journey where I will be adding my own machine learning projects. I am strictly NOT using any AI to write or generate the code. AI tools are only used for project organization, scaffolding, and documentation. All ML scripts, models, and algorithms are handwritten entirely by me.

---

## Setup Instructions

Follow these steps to set up the development environment:

1. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment:**
   - **Windows:**
     ```bash
     .\venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables:**
   ```bash
   cp .env.example .env
   ```

---

## Learning Roadmap

This roadmap follows a progression from foundational concepts to advanced autonomous agents.

### Phase 1: Supervised Learning
- [ ] **01 Linear Regression** - Simple and Multiple Linear Regression.
- [ ] **02 Logistic Regression** - Binary and Multiclass Classification.
- [ ] **03 Decision Trees & Forests** - Tree-based models and Ensembles.
- [ ] **04 Support Vector Machines** - Linear and Non-linear classification.
- [ ] **05 K-Nearest Neighbors** - Instance-based learning.
- [ ] **06 Naive Bayes** - Probabilistic classifiers.
- [ ] **07 Ensemble Methods & Boosting** - AdaBoost, Gradient Boosting, XGBoost.

### Phase 2: Unsupervised Learning
- [ ] **01 Clustering Algorithms** - K-Means, Hierarchical, and DBSCAN.
- [ ] **02 Dimensionality Reduction** - PCA, t-SNE, and Feature Extraction.
- [ ] **03 Association Rules** - Apriori and Eclat.
- [ ] **04 Anomaly Detection** - Outlier and novelty detection.

### Phase 3: Deep Learning
- [ ] **01 Artificial Neural Networks (ANN)** - Multilayer Perceptrons.
- [ ] **02 Convolutional Neural Networks (CNN)** - Computer Vision tasks.
- [ ] **03 Recurrent Neural Networks (RNN)** - Sequence and Time-series data.

### Phase 4: Reinforcement Learning
- [ ] **01 Q-Learning** - Tabular RL methods.
- [ ] **02 Deep Q-Networks (DQN)** - Neural-network based RL agents.

---

## Directory Structure

- `01_supervised_learning/`: Standard supervised ML tasks.
- `02_unsupervised_learning/`: Pattern discovery in unlabeled data.
- `03_deep_learning/`: Neural network architectures and applications.
- `04_reinforcement_learning/`: Agent-based learning environments.
- `docs/`: Comprehensive documentation and notes (Obsidian/GitHub compatible).
- `requirements.txt`: Core ML stack (NumPy, Pandas, Scikit-learn, etc.).
