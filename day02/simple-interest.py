initial_balance = int(input("Initial balance: "))
time_years = int(input("Time in years: "))
interest_rate = float(input("Interest rate: "))

print(f"Initial Balance: PHP {initial_balance:,.2f}")
print(f"Time (in Years): {time_years:.4f}")
print(f"Interest Rate: {interest_rate:.4%}")

simple_interest = initial_balance * (1 + interest_rate) * time_years
print(f"Simple Interest: {simple_interest}")