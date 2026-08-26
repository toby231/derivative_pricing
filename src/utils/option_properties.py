import numpy as np
from dataclasses import dataclass

@dataclass
class Option:

    """
    A simple container for option parameters.
    Use as: r, T, n, S_0, K, sigma.
    """

    # Basic parameters

    S_0: float = 100.0 # Initial Stock Price
    K: float = 100.0 # Strike Price 
    r: float = 0.05 # Risk-free rate
    T: float = 1.0 # Time to maturity in years
    n: int = 1 # Number of steps
    sigma: float = 0.05 # Volatility

    def __post_init__(self):
        dt = self.T / self.n

        self.u = np.exp(self.sigma * np.sqrt(dt)) 
        self.d = np.exp(-self.sigma * np.sqrt(dt))