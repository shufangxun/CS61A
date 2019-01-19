def num_part(n, m) :
        if n == 0 :
            return 1
        elif n < 0 :
            return 0
        elif m == 0:
            return 0
        else :
            return num_part(n-m, m) + num_part(n, m-1)