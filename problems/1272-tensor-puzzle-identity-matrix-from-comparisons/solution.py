import numpy as np

def eye(n: int) -> np.ndarray:
    """n x n identity matrix without np.eye."""
    row = np.arange(n)
    col = np.arange(n)[:, None]
    return (row == col).astype(np.float64)
