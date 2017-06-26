import numpy as np
#from rbf_network_python import rbf_network
from rbf_network_cython import rbf_network

np.random.seed(0)
D = 5
N = 1000
X = np.array([np.random.rand(N) for d in range(D)]).T
beta = np.random.rand(N)
theta = 10

result = rbf_network(X, beta, theta)
print(result[0])
