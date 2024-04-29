'''
7.	A year is a leap year if it is divisible by 4,
unless it is a century year that is not divisible by 400.
(1800 and 1900 are not leap years while 1600 and 2000 are.)
Write a program that calculates whether a year is a leap year
'''

year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            year=True
        else:
            year=False
    else:
        year=True
else:
    year=False

print(year)