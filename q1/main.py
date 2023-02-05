import numpy as np
from matplotlib import pyplot as plt


# 1 t t^2
# -1 -0.5 0 0.5 1
A = [[1, -1, 1], [1, -0.5, 0.25], [1, 0, 0], [1, 0.5, 0.25], [1, 1, 1]]
# -20, 17, 42, 94, 127
T = [1, 0.5, 0, 0.5, 2]

A = np.array(A)
T = np.array(T)
At = np.transpose(A)
AtA = np.dot(At, A)
AtT = np.dot(At, T)
AtAI = np.linalg.inv(AtA)
W = np.dot(AtAI, AtT)

print(W)
# Scatter T and show W line
plt.scatter(A[:, 1], T)
print(np.dot(A, W))
print(A)
linSpace01 = np.linspace(-1.1, 1.1, 100)
plt.plot(linSpace01, np.dot([[1, x, x**2] for x in linSpace01], W), color='red')
# Label the graph
plt.xlabel('t')
plt.ylabel('y')


plt.savefig('q1.png')
