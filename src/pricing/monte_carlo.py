import numpy as np
from src.utils.option_properties import Option


def closed_form_monte_carlo(opt = Option,n_paths=10000,seed=None):
    if seed is not None:
        np.random.seed(seed)

    Z = np.random.standard_normal(n_paths)
    S_T = opt.S_0 * np.exp((opt.r - 0.5*opt.sigma**2)*opt.T + opt.sigma*np.sqrt(opt.T)*Z)
    payoff = np.maximum(S_T - opt.K, 0)
    price = np.exp(-opt.r*opt.T) * np.mean(payoff)
    return price