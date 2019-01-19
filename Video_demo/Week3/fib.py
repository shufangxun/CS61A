def fib1(n):
    """
    iteration version
    """

    pred, curr = 1, 0    #计算fib(0)
    k = 0
    """
    pred, curr = 0, 1
    k = 1
    """
    while k<n:
        pred, curr = curr, curr+pred
        k = k+1
    return curr


def fib2(n):
    """
    recursion version
    """
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        return fib2(n-1) + fib2(n-2)


