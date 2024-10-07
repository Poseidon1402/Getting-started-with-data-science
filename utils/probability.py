import math
SQRT_TWO_PI = math.sqrt(2 * math.pi)

def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (SQRT_TWO_PI * sigma))
    
def inverse_normal_cdf(p: float,
                    mu: float = 0,
                    sigma: float = 1,
                    tolerance: float = 0.00001) -> float:
    """find approximate inverse using binary search"""
    # if distribution is not standard, first standardize it
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    
    low_z = -10.0 # normal_cdf(-10) is very close to 0
    hi_z = 10.0 # normal_cdf(-10) is very close to 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2 # consider the mid-point
        mid_p = normal_cdf(mid_z) # and the CDF value there
    if mid_p < p:
        low_z = mid_z # the mid-point is still too low, search above it
    else:
        hi_z = mid_z # the mid-point is still too high, search below it
    return mid_z