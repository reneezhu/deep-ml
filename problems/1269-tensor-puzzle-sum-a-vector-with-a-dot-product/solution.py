import numpy as np

def vector_sum(a: np.ndarray):
    """Sum elements of 1-D array a without np.sum / loops."""
    # Your code here
    b = np.arange(a.shape[0]) * 0.0 + 1.0
    return np.dot(a, b)
