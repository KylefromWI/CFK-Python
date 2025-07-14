year = int(input("What year is it?"))
month = input("What month is it?")
year_1 = None
c = None
year_1 = year - 700
year_1 * 365
num_leap_year = (year // 4) - (year % 100 == 0 and year % 400 != 0)
num_days = year_1 + num_leap_year + 1
if year % 4 == 0:
    leap_year = "Leap Year"
else:
    leap_year = "Not a Leap Year"

month_days = {
    "January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30,
    "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}
if leap_year == "Leap Year":
    month_days["February"] = 29


if month == "January":
    num_days = num_days + 0
if month == "February":
    num_days = num_days + 31
if month == "March":
    num_days = num_days + 59
if month == "April":
    num_days = num_days + 89
if month == "May":
    num_days = num_days + 119
if month == "June":
    num_days = num_days + 150
if month == "July":
    num_days = num_days + 180
if month == "August":
    num_days = num_days + 211
if month == "Spetmber":
    num_days = num_days + 242
if month == "October":
    num_days = num_days + 272
if month == "November":
    num_days = num_days + 303
if month == "December":
    num_days = num_days + 333

if num_days % 7 == 1:
    c = 1
elif num_days % 7 == 2:
    c = 2
elif num_days % 7 == 3:
    c = 3
elif num_days % 7 == 4:
    c = 4
elif num_days % 7 == 5:
    c = 5
elif num_days % 7 == 6:
    c = 6
else:
    c = 7
print("              ",year,"              ")
print("              ",month,"              ")
if c > 7:
    print("invalid input")
print("Sun  Mon  Tue  Wed  Thu  Fri  Sat")
x = 1
for rows in range(1,7):        
    for col in range(1,8):
        if rows == 1 and col == c:
            print("{:02d}".format(x), end="   ")
            x = x + 1
        elif col > c:
            print("{:02d}".format(x), end="   ")
            x = x + 1
        elif rows > 1:
            print("{:02d}".format(x), end="   ")
            x = x + 1
        else:
            print("  ", end="   ")
        if x > month_days[month]:
            break
    print ('')
    if x > month_days[month]:
        break
Month_Calendar.py
Displaying RouletteGame.py.
