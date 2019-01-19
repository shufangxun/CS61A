def handle_overflow(s1, s2):
	"""
	>>> handle_overflow(27, 15)
	No overflow
	>>> handle_overflow(35, 29)
	Move to Section 2: 1
	>>> handle_overflow(20, 32)
	Move to Section 1: 10
	>>> handle_overflow(35, 30)
	No space left in either section
	"""
	if s1 < 30 and s2 < 30:
		print("No overflow")
		return
	elif s1 > 30 and s2 < 30:
		move1 = 30 - s2 
		print("Move to Section 2: {}".format(move1))
		return
	elif s1 < 30 and s2 > 30:
		move2 = 30 - s1
		print("Move to Section 1: {}".format(move2))
		return
	else:
		print("No space left in either section")
		return
