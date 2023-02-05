import numpy as np
import matplotlib.pyplot as plt

D = [0, 1, 5, 10]

for d in D:
    M = np.random.normal(0, 1, (500, 500))
    np.fill_diagonal(M, -d)

    eigenvalues = np.linalg.eigvals(M)
    real = np.real(eigenvalues)
    imag = np.imag(eigenvalues)

    plt.scatter(real, imag)
    plt.xlabel('Real(λ)')
    plt.ylabel('Imag(λ)')
    plt.title(f'D={d}')
    plt.show()
