def wear_jacket(temp, raining):
	"""
	>>> wear_jacket(90, False)
	False
	>>> wear_jacket(40, False)
	True
	>>> wear_jacket(100, True)
	True
	"""
	return temp < 60 or raining == True
