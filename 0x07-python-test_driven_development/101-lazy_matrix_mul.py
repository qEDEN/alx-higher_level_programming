#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    try:
        result = np.dot(np.array(m_a), np.array(m_b))
        return result.tolist()
    except ValueError as e:
        raise ValueError("Matrices cannot be multiplied") from e