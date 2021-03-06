def calculator(number1, number2, operator):
	"""function that takes two numbers with whatever specific operator and return the output """
	if operator == "+":
		total = number1 + number2
	elif operator == "-":
		total = number1 - number2
	elif operator == "*":
		total = number1 * number2
	elif operator == "/":
		total = number1 / number2
	elif operator == "**":
		total = number1 ** number2
	elif operator == "//":
		total = number1 // number2
	return total
def input_output():
	""" This function takes the input from the user of the numbers and operator and then returns out the output.
	The function also asks if you want to continue. """
	a = True
	while a:
		number1 = input("Enter the first number: ")
		number2 = input("Enter the second number: ")
		operator = input("Enter the operator: ")

		number1 = float(number1)
		number2 = float(number2)
		results = calculator(number1, number2, operator)
		# checking if the output is a float
		if (not isinstance(results,float)):
			return False
		print(results)
		# gets the input of the user to continue or not
		a = input("Do you want to exit (Y/N): ")
		if (a == "n" or a == "N"):
			continue
		else:
			break
