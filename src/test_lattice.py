import numpy as np
import matplotlib.pyplot as plt


x1 = np.arange(10)
x2 = np.arange(10)
lattice = np.array([(x1_, x2_) for x1_ in x1 for x2_ in x2])
plt.scatter(lattice[:, 0], lattice[:, 1])

phi_tilde = np.pi / 4
theta = np.pi / 6
distort = np.array([
    [np.cos(phi_tilde), np.sin(phi_tilde)],
    [np.cos(theta) * np.cos(phi_tilde) - np.sin(theta) * np.sin(phi_tilde),
     np.cos(theta) * np.sin(phi_tilde) + np.sin(theta) * np.cos(phi_tilde)
    ]
])
stretch = np.array([[1.0, 0], [0, 1.0]])
transformation = stretch @ distort
lattice_tilde = lattice @ transformation
plt.scatter(lattice_tilde[:, 0], lattice_tilde[:, 1])
# TODO: Calculate volume
plt.show()
