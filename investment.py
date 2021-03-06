def calculate_apr(principal, interest_rate, years):
	""" Calculate the value of the investment after a certain amount of years. 
	Takes principal, interest_rate, and years input and returns output. """
	# Using if statements to check if inputs are invald with negative numbers
	if principal < 0:
		return False
	if interest_rate < 0:
		return False
	if years < 0:
		return False
	output = 0
	for i in range(years):
		# equation used to calculate the total investments
		output = principal * (1 + interest_rate)**years
		return output

