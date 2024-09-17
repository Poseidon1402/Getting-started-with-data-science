from typing import List

Vector = List[float]

def dot(v: Vector, w: Vector) -> float:
    """Compute v_1 * w_1 + ... + v_n * w_n"""
    assert len(v) == len(w), "Vectors must be same length"
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

assert dot([1, 2, 3], [4, 5, 6]) == 32

def sum_of_squares(v: Vector) -> float:
    """Return v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)