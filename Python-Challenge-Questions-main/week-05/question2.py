month_days = {
    "January": 31,
    "February": 28,  # 29 days in a leap year
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

print("Welcome to days in a month calculator...")
user_month = input("Enter a month:\n").title()


if user_month in month_days:
    if user_month == "February":
        print(f"There are {month_days[user_month]} days in {user_month} (29 in a leap year).")
    else:
        print(f"There are {month_days[user_month]} days in {user_month}.")
else:
    print("The month is invalid.")
