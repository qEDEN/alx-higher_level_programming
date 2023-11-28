def pow(a, b):
    result = 1

    # If the exponent is negative, compute the reciprocal
    if b < 0:
        a = 1 / a
        b = -b

    # Multiply 'a' by itself 'b' times
    for _ in range(b):
        result *= a

    return round(result, 2)

# Test cases
print(pow(0.1, -2))
