from operator import floordiv, mod

def divide(n, d):
    """
    >>> q, r = divide(2013, 10)
    >>> q
    201
    >>> r
    3
    """
    return floordiv(n, d), mod(n, d)


