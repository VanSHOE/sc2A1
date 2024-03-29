import numpy as np
import matplotlib.pyplot as plt

D = [0, 1, 5, 10]

for d in D:
    M = np.random.normal(0, 1, (500, 500))

    # for i in range(500):
    #     for j in range(i):
    #         M[i][j] = -M[j][i]

    np.fill_diagonal(M, -d)
    print(M)

    eigenvalues = np.linalg.eigvals(M)
    real = np.real(eigenvalues)
    imag = np.imag(eigenvalues)

    plt.scatter(real, imag)
    plt.xlabel('Real(λ)')
    plt.ylabel('Imag(λ)')
    plt.title(f'D={d}')
    plt.savefig(f'M_D_SkewWithConstantD={d}.png')
    plt.show()
