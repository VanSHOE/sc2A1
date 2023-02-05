import numpy as np
import matplotlib.pyplot as plt

# Define A matrix and T array
A = [[1, -1, 1], [1, -0.5, 0.25], [1, 0, 0], [1, 0.5, 0.25], [1, 1, 1]]
T = [1, 0.5, 0, 0.5, 2]

# Convert lists to numpy arrays
A = np.array(A)
T = np.array(T)

# Calculate the transpose of A
At = np.transpose(A)

# Calculate AtA and AtT
AtA = np.dot(At, A)
AtT = np.dot(At, T)

# Calculate the inverse of AtA
AtAI = np.linalg.inv(AtA)

# Calculate W
W = np.dot(AtAI, AtT)

# Print the calculated W
print("W:", W)

# Plot the scatter plot of T against A[:, 1]
plt.scatter(A[:, 1], T)

# Calculate the dot product of A and W and print it
dot_product = np.dot(A, W)
print("Dot product of A and W:", dot_product)

# Generate 100 evenly spaced numbers between -1.1 and 1.1
linSpace01 = np.linspace(-1.1, 1.1, 100)

# Plot the line of the dot product of [1, x, x**2] and W
plt.plot(linSpace01, np.dot([[1, x, x ** 2] for x in linSpace01], W), color='red')

# Label the x-axis and y-axis
plt.xlabel('t')
plt.ylabel('y')

# Save the figure
plt.savefig('q1.png')
