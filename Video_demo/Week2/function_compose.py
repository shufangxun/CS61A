def  make_adder(n):
        def adder(k):
                return k + n
        return adder

def  suqre(x):
        return x*x
 
def  triple(x):
        return 3*x

def  compose(f, g):
        def  h(x):
                return f(g(x))
        return h


