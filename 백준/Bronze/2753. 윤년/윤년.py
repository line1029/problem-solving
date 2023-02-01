def leap_year(year):
    if year % 4 or (not year % 100 and year % 400):
        return 0
    return 1


print(leap_year(int(input())))
