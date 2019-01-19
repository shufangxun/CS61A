def cascade(n):
    print(n)
    if n > 0 :
        cascade(n // 10)
        print(n)
    """
    if n < 10 :
        print(n)
    else :
        print(n)
        cascade(n // 10)
        print(n)
    """
def inverCascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n : f_then_g(grow, print, n // 10)
shrink = lambda n : f_then_g(print, shrink, n //10)
