def keep_ints(n):
	"""Returns a function which takes one parameter cond and prints out
	all integers 1..i..n where calling cond(i) returns True.
	>>> def is_even(x):
	... # 	Even numbers have remainder 0 when divided by 2.
	... 	return x % 2 == 0
	>>> keep_ints(5)(is_even)
	2
	4
	"""
	def gone(condi):
		k = 2
		while k < n:
			if condi(k):
				print(k)
			k += 1
	return gone
