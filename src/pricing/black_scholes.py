import numpy as np
from scipy.stats import norm
from src.utils.option_properties import Option

# I want to create a function that applies the closed form solution of the Black Scholes differential equation. There is no analytic solution for the American option.

def closed_form_black_scholes(opt = Option, option_class = "call"):
    d1 = (np.log(opt.S_0 / opt.K) + (opt.r + opt.sigma**2/2)*opt.T)/(opt.sigma*np.sqrt(opt.T))
    d2 = d1 - opt.sigma*np.sqrt(opt.T)
    if option_class == "call":
        return opt.S_0 * norm.cdf(d1) - opt.K * np.exp(-opt.r*opt.T)*norm.cdf(d2)
    else:
        return opt.K * np.exp(-opt.r*opt.T)*norm.cdf(-d2) - opt.S_0 * norm.cdf(-d1)
