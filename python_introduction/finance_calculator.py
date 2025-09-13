# finance_calculator.py

# User Input for Financial Details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# Project Annual Savings with 5% Interest
annual_savings = monthly_savings * 12
projected_annual_savings = annual_savings + (annual_savings * 0.05)

# Output Results
print(f"\nYour monthly savings: ${monthly_savings:.2f}")
print(f"Projected savings after one year with 5% interest: ${projected_annual_savings:.2f}")
