def gcd1(a, b) :
        """
        Eculidean algorithm -- recursion version1
        """
        if b == 0 :
            return a
        elif a < b :
            return gcd1(b, a)
        elif a % b == 0 :
            return b
        else :
            return gcd1(b, a%b)

            """
        ## Eculidean algorithm -- recursion version2--in C
        if a < b :
            return gcd2(b, a)
        else :
            return b == 0 ? a : gcd2(b, a % b)
            """

def gcd2(a, b) :
        """
        Eculidean algorithm -- iteration version
        """
        if b == 0 :
            return a
        elif a < b :
            return gcd2(b, a)
        else :
            while(b != 0) :
                a, b = b, a % b
            return a

def gcd3(a, b):
        """
         minus version
        """
        if b == 0:
            return a
        if a % b == 0:
            return b
        elif  a < b :
            return gcd3(b, a)
        else :
            return gcd3(b, a-b)

def  lcm(a, b):
         return  a * b // gcd1(a, b)
