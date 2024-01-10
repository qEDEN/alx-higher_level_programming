#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Returns:
        numpy.ndarray: The resulting matrix.

    Raises:
        ValueError: If the matrices cannot be multiplied.

    Example:
    >>> lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
    array([[ 7, 10],
           [15, 22]])

    >>> lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]])
    array([[13, 16]])
    """
    try:
        result = np.dot(np.array(m_a), np.array(m_b))
        return result.tolist()
    except ValueError as e:
        raise ValueError("Matrices cannot be multiplied") from e