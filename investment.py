def calculate_apr(principal, interest_rate, years):
	principal = float(principal)
	interest_rate = float(interest_rate)
	years = float(years)
	if principal < 0:
		return False
	if interest_rate < 0:
		return False
	if years < 0:
		return False
	output = 0
	for i in range(years):
		output = ((principal)*((1+interest_rate)**(years)))
	if output == True:
		return output
	else:
		return False


