def calculator(number1, number2, operator):
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
	a = True
	while a:
		number1 = input("Enter the first number: ")
		number2 = input("Enter the second number: ")
		operator = input("Enter the operator: ")

		number1 = float(number1)
		number2 = float(number2)
		results = calculator(number1, number2, operator)
		if (not isinstance(results,float)):
			return False
		print(results)
		a = input("Do you want to exit (Y/N): ")
		if (a == "n" or a == "N"):
			continue
		else:
			break
input_output()
