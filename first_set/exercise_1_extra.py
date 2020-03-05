day_int = int(input("What day of the week is it? (number please)"))

day_int = day_int % 7   # make sure the number is between 0 and 6

if day_int == 0:        # note the double "="-sign
    day = "Sunday"
elif day_int == 1:
    day = "Monday"
elif day_int == 2:
    day = "Tuesday"
elif day_int == 3:
    day = "Wednesday"
elif day_int == 4:
    day = "Thursday"
elif day_int == 5:
    day = "Friday"
else:
    day = "Saturday"

print("Today is", day)