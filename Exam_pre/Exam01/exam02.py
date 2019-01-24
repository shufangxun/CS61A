def sandwich(n):
    """
        Return True if n contains a sandwich and False otherwise
        >>> sandwich(416263) # 626
        True
        >>> sandwich(5050) # 505 or 050
        True
        >>> sandwich(4441) # 444
        True
        >>> sandwich(1231)
        False
        >>> sandwich(55)
        False
        >>> sandwich(4456)
        False
    """
    tens, ones = n // 10 % 10, n % 10
    n = n // 100
    while n:
        if n % 10 == ones:
            return True
        else:
            tens, ones = n % 10, tens
            n = n // 10
    return False