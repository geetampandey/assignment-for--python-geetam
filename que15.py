#Calculate compound interest
#Input: principal = 10000, rate = 5, time = 2
#Output: Compound Interest = ?
# Input values
principal = 10000
rate = 5
time = 2

# Formula
amount = principal * (1 + rate/100) ** time
compound_interest = amount - principal

# Output
print("Compound Interest =", compound_interest)