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

def add(v: Vector, w: Vector) -> Vector:
    """Add corresponding elements"""
    assert len(v) == len(w), "Vector should be have the same length"
    return [v_i + w_i for v_i, w_i in zip(v, w)]
    
def scalar_multiply(c: float, v: Vector) -> Vector:
    """Multiply every element by c"""
    return [c * v_i for v_i in v]