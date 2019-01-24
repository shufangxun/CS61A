def mul_recursive(m, n) :
    """
    Write a function that takes two numbers m and n and returns their product.
    Assume m and n are positive integers. Use recursion, not mul or *!
    Hint: 5*3 = 5 + 5*2 = 5 + 5 + 5*1.
    """
        if n == 0:
            return 0
        if n == 1:
            return m
        if n < 0 and m >= 0 :
            return - mul_recursive(m, -n)
        if m < 0 and n >= 0 :
            return - mul_recursive(-m, n)
        if m < 0 and n < 0 :
            return mul_recursive(-m, -n)
        else :
            return m + mul_recursive(m ,n - 1)