def double_eights(n):
    k = 0
    while n > 0 :
        if n % 10 == 8:
            k += 1
            if k >= 2 :
                break
        else :
            k = 0
        n = n // 10
    if k >= 2 :
        return True
    else:
        return False