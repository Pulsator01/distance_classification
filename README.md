# distance_classification
 MLPR assignment

## 📚 Report

### 1. What are the common distance metrics used in distance-based classification algorithms? 

- Euclidean Distance
- Manhattan Distance
- Minkowski Distance
- Chebyshev Distance
- Cosine Distance
- Hamming Distance
- Mahalanobis Distance

---

### 2. What are some real-world applications of distance-based classification algorithms? 

- Image Recognition
- Recommendation Systems
- Text Classification
- Medical Diagnosis
- Anomaly Detection
- Genetics

---

### 3. Explain various distance metrics. 

#### Euclidean Distance:
\[
d(p, q) = \sqrt{\sum_{i=1}^n (p_i - q_i)^2}
\]
This metric measures the straight-line distance between two points in n-dimensional space. It is widely used in tasks such as clustering and classification.

#### Manhattan Distance:
\[
d(p, q) = \sum_{i=1}^n |p_i - q_i|
\]
Also known as L1 distance, it is useful for calculating distances in grid-based systems, as it measures the sum of the absolute differences between coordinates.

#### Minkowski Distance:
\[
d(p, q) = \left(\sum_{i=1}^n |p_i - q_i|^p\right)^{1/p}
\]
Minkowski distance is a generalization of both Euclidean (p=2) and Manhattan (p=1) distances. When the parameter p approaches infinity, it becomes the Chebyshev distance.

#### Chebyshev Distance:
\[
d(p, q) = \max(|p_i - q_i|)
\]
This distance metric calculates the maximum absolute difference along any coordinate dimension. It is commonly used in board games like chess to determine the minimum number of moves needed for a king.

#### Cosine Distance:
\[
\text{similarity}(A, B) = \frac{A \cdot B}{\|A\|\|B\|}
\]
Cosine distance evaluates the angle between two vectors rather than their magnitude. It is particularly effective in high-dimensional spaces, such as those encountered in text classification tasks.

#### Hamming Distance:
Hamming distance counts the number of differing elements between two binary vectors. It is often used in error detection and correction algorithms.

#### Mahalanobis Distance:
\[
d_M(p, q) = \sqrt{(p-q)^T S^{-1} (p-q)}
\]
Mahalanobis distance considers both the variance of each feature and the correlations between features, making it effective when the dataset includes variables with different scales or correlated features.

---

### 4. What is the role of cross-validation in model performance? 

Cross-validation is a technique used to evaluate a model’s performance. It helps to reduce overfitting by training the model on different subsets of the data, leading to better generalization to new, unseen data. By providing a more robust evaluation through multiple splits of the dataset, cross-validation offers a more accurate estimate of model performance. Additionally, it is useful for tuning hyperparameters by comparing validation scores across different parameter configurations.

---

### 5. Explain variance and bias in terms of KNN? 

#### Variance in KNN:
When the value of K is small, the KNN algorithm can become overly sensitive to noise in the data. This high variance might cause the model to fit the training data too closely, which can lead to overfitting. Overfitting generally results in good performance on training data but poor generalization to new data.

#### Bias in KNN:
In contrast, when K is large, the model may become too generalized. High bias in the model causes it to consider too many neighbors when making predictions, leading to underfitting. Underfitting occurs when the model fails to capture important patterns in the data, often resulting in poor performance on both training and testing datasets.

#### Balancing Bias and Variance:
Finding the right balance between bias and variance involves choosing a moderate value of K. Using cross-validation techniques can help identify the optimal K value that minimizes prediction error and improves model performance.
