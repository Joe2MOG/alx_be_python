# Prompt the user to enter their current age
current_age = int(input("How old are you? "))

# Calculate how old the user will be in 2050
year_now = 2023
future_year = 2050
years_to_future = future_year - year_now
future_age = current_age + years_to_future

# Print the result
print(f"In {future_year}, you will be {future_age} years old.")