import numpy as np

# Sample dataset (multiple features)
X = np.array([
    [2100, 3],
    [1600, 2],
    [2400, 4],
    [1416, 2],
    [3000, 4]
])

y = np.array([400000, 330000, 369000, 232000, 540000])

# Number of samples
m = X.shape[0]

# Add bias column (x0 = 1)
X_b = np.c_[np.ones((m, 1)), X]

# Initialize theta values
theta = np.zeros(X_b.shape[1])  # [theta0, theta1, theta2]

# Hyperparameters
alpha = 0.00000001   # learning rate (very small due to large y values)
epochs = 10000

# Gradient Descent
for i in range(epochs):
    y_pred = X_b.dot(theta)
    gradients = (1/m) * X_b.T.dot(y_pred - y)
    theta = theta - alpha * gradients

print("Final theta values:", theta)

# Predict price for 2000 sq ft, 3 rooms
new_data = np.array([1, 2000, 3])
pred = new_data.dot(theta)

print("Predicted price:", pred)
