# 🧮 Age Calculator
# This program tells your exact age using your birth date

from datetime import date

try:
    # Ask user for complete date of birth
    birth_year = int(input("Enter your birth year (e.g. 2012): "))
    birth_month = int(input("Enter your birth month (1-12): "))
    birth_day = int(input("Enter your birth day (1-31): "))

except ValueError:
    print("Invalid Input! Enter Numbers only.")
    exit()

today = date.today()

# Validate inputs (logical checks)
if birth_year < 1900 or birth_year > today.year:
    print("Please enter realistic birth year: ")
    exit()
if birth_month < 1 or birth_month > 12:
    print("Please enter a realistic birth month: ")
    exit()
if birth_day < 1 or birth_day > 31:
    print("Please enter a realistic birth day: ")
    exit()

# Create a date object for birth date
try:
    birth_date = date(birth_year, birth_month, birth_day)
except ValueError:
    print("Invalid date combination (e.g. Feb 30 doesn't exist).")
    exit()

# ------ Calculate exact age ---------
age_years = today.year - birth_year
age_months = today.month - birth_month
age_days = today.day - birth_day

# Adjust if current month/day is before birth month/day
if age_days < 0:
    age_months -= 1
    # Borrows day from previous month
    previous_month = (today.month - 1) or 12
    previous_year = today.year if today.month != 1 else today.year - 1
    days_in_prev_month = date(previous_year, previous_month % 12 + 1, 1) - date(previous_year, previous_month, 1).day
    age_days += days_in_prev_month

if age_months < 0:
    age_years -= 1
    age_months += 12

# Output
print("\n" + "=" * 40)
print(f"🎂 You are {age_years} years, {age_months} months, and {age_days} days old.")
print(f"📅 Today's Date: {today.strftime('%d %B %Y')}")
print("=" * 40 + "\n")