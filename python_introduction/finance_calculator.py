#Projecting user's monthly savings to a year with an annual interest rate of 5%
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter you monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
print("Your monthly savings are: $", monthly_savings, ".")
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)
print("Projected savings after one year, with interest, is: $", projected_savings, ".")
