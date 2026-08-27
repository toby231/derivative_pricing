import numpy as np

from src.utils.option_properties import Option
from src.utils.greeks import delta_hedge

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
    delta = delta_hedge(f_u,f_d,opt)
    return f, delta

def multistep(opt = Option, option_class = "call",option_type = "European"):
    if option_class not in ("call","put"):
        raise ValueError(f"Invalid option class. Must be 'call' or 'put'.")
    if option_type not in ("European","American"):
        raise ValueError(f"Invalid option type. Must be 'American' or 'European'.")

    j = np.arange(opt.n + 1)
    S_T = opt.S_0 * opt.u**j * opt.d**(opt.n - j)

    if option_class == "call":
        values = np.maximum(S_T - opt.K, 0)
    else:
        values = np.maximum(opt.K - S_T, 0)

    discount = np.exp(-opt.r * opt.T/opt.n)
    p = (np.exp(opt.r * opt.T / opt.n) - opt.d) / (opt.u - opt.d)

    for step in range(opt.n,0,-1):
        values = discount * (p * values[1:] + (1-p)*values[:-1])
        if option_type == "American":
            j = np.arange(step)
            S = opt.S_0 * opt.u**j * opt.d**(step - 1 - j)

            continuation = values
            intrinsic = np.maximum(S - opt.K, 0) if option_class == "call" else np.maximum(opt.K - S, 0)
            values = np.maximum(continuation, intrinsic)

    return values[0]
        