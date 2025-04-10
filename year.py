def is_leap_year(year):
    return (year % 4 ==0 and year % 100 !=0) or (year % 400 ==0)
user_input = input("Enter Year ")

try:
    year=int(user_input)
    if is_leap_year (year):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is a not leap year")
except ValueError:
    print("Please enter a valid number.")