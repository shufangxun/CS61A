def delay(arg) :
    """
    return the arg: maybe function
    """
    print("delayed")
    def g() :
        return arg
    return g

def suqre(x):
        return x*x

def a(x) :
    """
    local argument
    """
    print("hello")
    def b(x) :
        return x
    return b
