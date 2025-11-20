import numpy as np
from numpy.linalg import norm

def cosine_sim(a, b):
    a = np.array(a)
    b = np.array(b)
    if norm(a) == 0 or norm(b) == 0:
        return 0.0
    return float(np.dot(a, b) / (norm(a) * norm(b)))
