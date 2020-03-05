days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

day_int = int(input("What day of the week is it? (number please)"))

print(days[day_int % 7])
