def is_year_leap(year):
    leap = False

    if year % 4 == 0:
        leap = True

        if year % 100 == 0 and year % 400 != 0:
            leap = False

    return leap


def days_in_month(year, month):
    feb = 28

    if is_year_leap(year):
        feb += 1

    return [31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month-1]


def day_of_year(year, month, day):
    days = 0

    for i in range(1, month):
        days += days_in_month(year, i)

    days += day
    return days


print(day_of_year(2000, 12, 31))
print(day_of_year(1999, 12, 31))
print(day_of_year(2000, 1, 1))
