#Calculating user's age in 2050 assuming the current year is 2023
current_year = 2023
future_year = 2050
user_age = int(input("How old are you? "))
user_age_in_future = user_age + (future_year - current_year)
print(f"In {future_year}, you will be {user_age_in_future} years old.")