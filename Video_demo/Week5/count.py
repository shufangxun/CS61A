def count(s,v):
    """
    count the number of v in s
    >>> count([1,2,1,2,3,4,8],1)
    2
    """

    count = 0
    for element in s:
        if element == v:
            count += 1 
    return count
