import numpy as np

def vstack(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Stack 1-D arrays a and b as rows of a (2, n) matrix."""
    # Your code here
    mask = (np.arange(2)[:, None] == 0) * 1   # shape (2, 1): [[1], [0]]
    return mask * a + (1 - mask) * b
