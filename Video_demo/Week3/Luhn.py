def split(n):
	return n // 10, n % 10

def sum_digits(n):
	next_n, last_digit = split(n)
	if n < 10 :
		return n
	else :
		return sum_digits(next_n) + last_digit

def Luhn_double_sum(n):
	next_n, last_digit = split(n)
	even_value = sum_digits(2 * last_digit)
	if n < 10 :
		return even_value
	else :
		return Luhn_sum(next_n) + even_value

def Luhn_sum(n):
	if n < 10 :
		return n
	else :
		next_n, last_digit = split(n)
		return Luhn_double_sum(next_n) + last_digit



