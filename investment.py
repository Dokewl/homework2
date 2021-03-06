def calculate_apr(principal, interest_rate, years):
	p = int(principal)
	i = float(interest_rate)
	y = int(years)
	if p < 0:
		return False
	if i < 0:
		return False
	if y < 0:
		return False
	total = 0
	for i in range(years):
		total = total + (principal * (1 + interest_rate))
	if total:
		print(total)
	else:
		total = False
calculate_apr(p,i,y)

