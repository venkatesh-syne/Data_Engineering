def leap_year(number):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return "leap year"
    else:
        return "not a leap year"
year = int(input("Enter the year: "))
print(leap_year(year))
