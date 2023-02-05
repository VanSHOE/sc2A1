import numpy as np
import matplotlib.pyplot as plt

# Define A matrix and T array
A = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [1, -1, 0, 0], [1, 0, -1, 0], [1, 0, 0, -1], [0, 1, -1, 0],
     [0, 1, 0, -1], [0, 0, 1, -1]]
b = [2.95, 1.74, -1.45, 1.32, 1.23, 4.45, 1.61, 3.21, 0.45, -2.75]

# Convert lists to numpy arrays
A = np.array(A)
b = np.array(b)

# Calculate the transpose of A
At = np.transpose(A)

# Calculate AtA and Atb
AtA = np.dot(At, A)
Atb = np.dot(At, b)

# Calculate the inverse of AtA
AtAI = np.linalg.inv(AtA)

# Calculate W
W = np.dot(AtAI, Atb)

# Print the calculated W
print("W:", W)
