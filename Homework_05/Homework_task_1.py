def is_year_leap(year: int):
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0


assert is_year_leap(1999) == False
assert is_year_leap(2000) == True
assert is_year_leap(1700) == False
assert is_year_leap(2004) == True
