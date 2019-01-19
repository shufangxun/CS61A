def  end(n, d):
        """
        >>>end(345678)
        8
        7
        6
        5
        """ 
        while n > 0:
                last, n = n%10, n // 10
                print(last)
                if  d == last:
                    return None
    
