def  search(f):
        x = 0
        while True:
                if  f(x):
                        return  x
                x += 1

        """
        while not f(x) :
                x += 1
        return x

        """
def  is_three(x):
        return x == 3

def  positive(x):
        return max(0, squre(x) - 100)

def squre(x):
        return x * x

def  inverse(f):
        return  lambda y :  search(lambda x : f(x) == y)


