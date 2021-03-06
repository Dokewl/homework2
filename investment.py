
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
	output = 0
	for i in range(years):
		output = output + ((principal)*(1+interest_rate))
		output = float(output)
	if output == True:
		return output
	else:
		return False
calculate_apr(principal, interest_rate, years)

