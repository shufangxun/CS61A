def identify(k):
    return k

def cube(k):
    return pow(k,3)

def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k+1
    return total
 
def sum_natural(n):
    return summation(n,identify)

def sum_cube(n):
    return summation(n,cube)

