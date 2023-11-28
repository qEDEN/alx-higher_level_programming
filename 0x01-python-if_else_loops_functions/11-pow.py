#!/usr/bin/python3
def pow(a, b):
    """
    Computes the value of a^b.

    Args:
    - a: base
    - b: exponent

    Returns:
    - The result of a^b
    """
    result = 1

    # Handle the case when base is 0 and exponent is negative
    if a == 0 and b < 0:
        return 0

    # If the exponent is negative, compute the reciprocal
    if b < 0:
        a = 1 / a
        b = -b

    # Multiply 'a' by itself 'b' times
    for _ in range(b):
        result *= a

    # Round to two decimal places if necessary
    if result % 1 == 0:
        return int(result)
    else:
        return round(result, 2)