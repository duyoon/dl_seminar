import numpy as np
from rbf_network_cython import rbf_network

np.random.seed(0)
D = 5
N = 1000
X = np.ones((N,D))
beta = np.random.rand(N)
beta = np.ones_like(beta)
theta = 1.0

result = rbf_network(X, beta, theta)
print(result[0])
