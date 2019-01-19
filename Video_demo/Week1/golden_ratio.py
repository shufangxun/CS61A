def approx_eq(x, y, tolerance=1e-15):
    """
    >>> approx_eq(3,3.1)
    False

    """
    return abs(x-y) < tolerance

def golden_update(result):
    return 1/result + 1

def squre_close_to_successor(result):
    return approx_eq(result * result, result + 1)

def improve(update, close, result=1):
    """
    >>> improve(golden_update, squre_close_to_successor)
    1.6180339887498951
    """
    while not close(result):
        result = update(result)
    return result


