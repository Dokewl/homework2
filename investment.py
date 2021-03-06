def calculate_apr(principal, interest_rate, years):
	principal = int(principal)
	interest_rate = float(interest_rate)
	years = int(years)
	if principal < 0:
		return False
	if interest_rate < 0:
		return False
	if years < 0:
		return False
	if (principal !=  isintance(principal, int):
		return False
	if (principal != isinstance(principal, float):
		return False
	if (interest_rate != isinstance(interest_rate, float):
		return False
	if (years != isinstance(years, int):
		return False
	total = 0
	for i in range(years):
		total = total + (principal * (1 + interest_rate))
		total = float(total)
	output = isinstance(total, float)
	if output:
		print(total)
	else:
		total = False


