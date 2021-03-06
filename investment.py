def calculate_apr():
        print("Enter the amount of money you're starting with:")
        principal = int(input())
        if (principal < 0):
                return False
        print("Enter the rate per year in decimal form:")
        interest_rate = float(input())
        if (interest_rate < 0):
                return False
        print("Enter the amount of time you are investing the money:")
        years = int(input())
        if (years < 0):
             return False
        output = ((principal)*(1+interest_rate)**(years))
        print(f"The value of the investment is {output} after {years} number of years.")
calculate_apr()
