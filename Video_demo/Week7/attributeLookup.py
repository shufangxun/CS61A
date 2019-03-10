class A :
    """What would Python Display?

    >>> a = A()
    >>> b = B(1)
    >>> b.n = 5
    >>> C(2).n
    4
    >>> C(2).z
    2
    >>> a.z == C.z
    True
    >>> a.z == b.z
    False
    >>> b.z.z.z
    1
    """
    z = -1
    def f(self, x):
            return B(x-1)

class B(A) :
    n  = 4
    def __init__(self, y):
            if y :
                self.z = self.f(y)
            else :
                self.z = C(y+1)

class C(B):
    def f(self, x):
        return x
