from fractions import gcd

### high level --- rational arithmetic
def add_rational(x, y):
    return rational(numer(x) * denom(y) + numer(y) * denom(x), denom(x) * denom(y))

def mul_rational(x, y):
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def rational_are_equal(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)

def print_rational(x):
    print(numer(x),"/",denom(x))



### lower level --- constructor & selector             
def rational(n, d):
    """
    Construct a rational number ---N/D
    """
    g = gcd(n, d)
    return [n // g, d // g] #list

def numer(x):
    return x[0]

def denom(x):
    return x[1]


