import numpy as np
from src.utils.option_properties import Option

# Delta hedging

def delta_hedge(f_u,f_d, opt = Option):
    return (f_u - f_d) / (opt.S_0 * (opt.u-opt.d))