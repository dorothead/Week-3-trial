day_int = int(input("What day of the week is it? (number please)"))

if day_int == 0:        # note the double "="-sign
    print("Sunday")
elif day_int == 1:
    print("Monday")
elif day_int == 2:
    print("Tuesday")
elif day_int == 3:
    print("Wednesday")
elif day_int == 4:
    print("Thursday")
elif day_int == 5:
    print("Friday")
elif day_int == 6:
    print("Saturday")
else:
    print("Please give a number between 0 and 6")