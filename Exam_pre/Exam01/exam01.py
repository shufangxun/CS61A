def  longest_increasing_suffix(n):
    """
    Implement the longest_increasing_suffix function, which returns the longest
    suffix (end) of a positive integer that consists of strictly increasing digits.
    >>> longest_increasing_suffix(63134)
    134
    >>> longest_increasing_suffix(233)
    3
    >>> longest_increasing_suffix(5689)
    5689
    >>> longest_increasing_suffix(568901)
    # Note: 01 is the suffix, displayed as 1
    1
    """
    m, suffix, k = 10, 0, 1
    while n:
        n, last = n // 10, n % 10
        if  last < m:
            m, suffix, k = last, suffix + k * last, 10 * k
        else:
            return suffix
    return suffix