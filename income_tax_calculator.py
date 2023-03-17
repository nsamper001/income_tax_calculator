TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000
DEPENDENT_DEDUCTION = 3000

def calculate_tax(gross_income, num_dependents):
    taxable_income = gross_income - STANDARD_DEDUCTION - (num_dependents * DEPENDENT_DEDUCTION)
    if taxable_income < 0:
        taxable_income = 0
    income_tax = taxable_income * TAX_RATE
    return income_tax

# user input:
gross_income = float(input("Enter the gross income: "))
num_dependents = int(input("Enter the number of dependents: "))
income_tax = calculate_tax(gross_income, num_dependents)
print(f"The income tax is: ${income_tax:.2f}")
