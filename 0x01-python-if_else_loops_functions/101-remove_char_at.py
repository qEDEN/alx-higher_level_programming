#!/usr/bin/python3
def remove_char_at(s, n):
    """
    Creates a copy of the string, removing the character at the position n.

    Args:
    - s: input string
    - n: index of the character to be removed

    Returns:
    - The modified string
    """
    if n < 0 or n >= len(s):
        return s  # Return the original string if n is out of bounds

    return s[:n] + s[n+1:]

