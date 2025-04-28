def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(is_leap_year(2000))  # True
print(is_leap_year(1900))  # False
print(is_leap_year(2020))  # True
print(is_leap_year(2021))  # False
print(is_leap_year(2024))  # True
print(is_leap_year(2025))  # False
print(is_leap_year(2026))  # False
print(is_leap_year(2027))  # False