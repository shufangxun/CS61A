def is_prime(n):
	"""
	>>> is_prime(10)
	False
	>>> is_prime(7)
	True
	"""
	k = 2
	while k < n :
		if n % k == 0:
			break
		else :
			k += 1
	return (k >= n)

