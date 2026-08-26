import numpy as np

from utils.option_properties import Option

# Start off with one step binomial tree

def onestep(opt=Option, option_class = "call"):
    if option_class not in ("call","put"):
        raise ValueError(f"Invalid option class. Must be 'call' or 'put'.")

    Su = opt.S_0 * opt.u
    Sd = opt.S_0 * opt.d

    if option_class == "call":
        f_u = max(Su - opt.K, 0)
        f_d = max(Sd - opt.K, 0)

    elif option_class == "put":
        f_u = max(opt.K - Su, 0)
        f_d = max(opt.K - Sd, 0)

    p = (np.exp(opt.r * opt.T) - opt.d) / (opt.u - opt.d)

    f = np.exp(-opt.r * opt.T) * (p * f_u + (1-p) * f_d)

    return f
