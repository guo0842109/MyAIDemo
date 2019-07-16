import numpy as np
from sklearn.decomposition import PCA

M = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
M = np.array([[-1, -2], [-1, 0], [0, 0],  [2, 1], [0, 1]])
pca = PCA(n_components=2)
pca.fit(M)

print(pca.explained_variance_ratio_)