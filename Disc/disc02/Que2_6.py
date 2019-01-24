def count_stairs(n, k) :
        """
        number of stairs = n
        max step = k
        """
        if n == 0:
            return 1
        elif n >= k :
            i, sum = 1, 0
            while i <= k:
                sum += count_stairs(n - i, k)
                i += 1
        else :
            sum = count_stairs(n, n)
        return sum