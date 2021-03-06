def calculate_apr(principal, interest_rate, years):
	principle = int(principal)
	interest_rate = float(interest_rate)
	years = int(years)
	if principle < 0:
		return False
	if interest_rate < 0:
		return False
	if years < 0:
		return False
	total = 0
	for i in range(years):
		total = total + (principal * (1 + interest_rate))
	if total:
		print(total)
	else:
		total = False


