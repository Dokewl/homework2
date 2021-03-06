
def calculate_apr(principal, interest_rate, years):
	if principal < 0:
		return False
	if interest_rate < 0:
		return False
	if years < 0:
		return False
	output = 0
	for i in range(years):
		output = principal * (1 + interest_rate)**years
		return output

