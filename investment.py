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
	temp = (principal * (1 + interest_rate)**(years)):
	temp = isinstance(temp, float)
	if temp == True:
		print(temp)
	else:
		temp = False


