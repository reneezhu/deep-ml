import numpy as np

def cumsum(a: np.ndarray) -> np.ndarray:
    """Inclusive cumulative sum of 1-D array a without np.cumsum."""
    # Your code here
    col = np.arange(a.shape[0])
    row = np.arange(a.shape[0])[:,None]
    b = (row >= col).astype(np.float64)
    return np.sum(a * b, axis=1)
