Return to [[Deep_Learning]]

# Convolutional Neural Networks (CNN)

Convolutional Neural Networks are a specialized type of neural network designed for processing structured grid data, such as images.

## Core Concept
CNNs use **Convolutional Layers** to automatically learn spatial hierarchies of features. Instead of fully connected layers, they use filters (kernels) that slide over the input to detect patterns like edges, textures, and eventually complex objects.

Key components:
- **Convolutional Layer**: Feature extraction using kernels.
- **Pooling Layer**: Downsampling to reduce spatial dimensions (e.g., Max Pooling).
- **Fully Connected (Dense) Layer**: Final classification based on extracted features.

## Mathematical Intuition
The convolution operation for an image $I$ and kernel $K$ is defined as:
$$(I * K)(i, j) = \sum_{m} \sum_{n} I(i+m, j+n) K(m, n)$$

CNNs exploit three key ideas:
1. **Sparse Connectivity**: Neurons are only connected to a small region of the input.
2. **Parameter Sharing**: The same filter is used across the entire image.
3. **Equivariant Representations**: Patterns can be detected regardless of their position in the image.

## Use Cases
- Image classification.
- Object detection (YOLO, R-CNN).
- Facial recognition.

## Advantages & Disadvantages
- **Advantages**: State-of-the-art for computer vision, fewer parameters than MLPs for image data.
- **Disadvantages**: Requires significant computational power (GPUs), needs large labeled datasets.

# Quick Challenge
**Objective:** Build a CNN to classify images of 10 different objects (airplanes, cars, birds, etc.).
**Dataset:** `keras.datasets.cifar10`
**Evaluation Metric:** Aim for a **Test Accuracy** of at least **75%** (a good baseline for a simple architecture).
