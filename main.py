
age = input("What is your current age? ")
age_int=int(age)
years_left=90-age_int
months_left=12*years_left
days_left=365*years_left
weeks_left=years_left*52
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
