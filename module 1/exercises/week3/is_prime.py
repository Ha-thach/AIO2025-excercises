def is_prime(n: int) -> bool:
    """
    Check whether a given number is a prime number.

    A prime number is a positive integer greater than 1 
    that has exactly two distinct positive divisors: 1 and itself.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    factor = [(i + 1) for i in range(n) if n % (i + 1) == 0]
    return True if len(factor) == 2 else False
