import math

# Define the tax slabs and rates.
tax_slabs = [
  (0, 250000, 0),
  (250001, 500000, 5),
  (500001, 750000, 10),
  (750001, 1000000, 15),
  (1000001, 1250000, 20),
  (1250001, 1500000, 25),
  (1500001, 2000000, 30),
  (2000001, 5000000, 30.6),
  (5000001, 10000000, 34.6),
  (10000001, 15000000, 39.6),
  (15000001, 25000000, 42.7),
  (25000001, 50000000, 45.7),
  (50000001, 10000000000, 48.7)
]

# Define the deductions and exemptions.
deductions = [
  10000,
  50000,
  100000,
  200000,
  300000,
  400000,
  500000,
  600000,
  700000,
  800000
]

# Define the retiral benefits.
retiral_benefits = [
  50000,
  100000,
  150000,
  200000,
  250000,
  300000,
  350000,
  400000,
  450000,
  500000
]

# Define the annual variable components.
annual_variable_components = [
  100000,
  200000,
  300000,
  400000,
  500000,
  600000,
  700000,
  800000,
  900000,
  1000000
]

# Get the user input.
basic_income = float(input("Enter your basic income: "))
allowances = []
number_of_allowances = int(input("Enter the number of allowances: "))
for i in range(number_of_allowances):
  allowance = float(input("Enter the allowance amount: "))
  allowances.append(allowance)
provident_fund = float(input("Enter the provident fund amount: "))
gratuity_fund = float(input("Enter the gratuity fund amount: "))
annual_variable_component = float(input("Enter the annual variable component: "))

# Calculate the gross income.
gross_income = basic_income + sum(allowances) - provident_fund - gratuity_fund - annual_variable_component

# Calculate the taxable income.
taxable_income = gross_income - sum(deductions)

# Calculate the tax liability.
tax_liability = 0
for slab in tax_slabs:
  if taxable_income >= slab[0]:
    tax_liability += (taxable_income - slab[0]) * slab[2]
    taxable_income = slab[0]

# Print the total tax.
print("Your total tax liability is:", tax_liability)
