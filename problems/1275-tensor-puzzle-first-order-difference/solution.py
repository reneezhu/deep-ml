import numpy as np

def diff(a: np.ndarray) -> np.ndarray:
    """out[0]=a[0]; out[i]=a[i]-a[i-1] for i>0."""
    # Your code here
    i = np.arange(a.shape[0])
    return a-(i>0)*a[i-1]
