def calculate_apr(principal, interest_rate, years):
	if principal < 0:
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
calculate_apr(principal = int(input()), interest_rate = float(input()), years = int(input()))

