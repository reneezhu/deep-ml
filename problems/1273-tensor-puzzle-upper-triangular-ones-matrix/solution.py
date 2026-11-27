import numpy as np

def triu_ones(n: int) -> np.ndarray:
    """n x n upper-triangular matrix of ones (including diagonal)."""
    # Your code here
    col = np.arange(n)
    row = np.arange(n)[:, None]
    return (col >= row).astype(np.float64)
