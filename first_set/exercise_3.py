# test using these values
a = 19
b = 6
day = 3

# a
print((a > b) != (a <= b))

# b
print((a >= b) != (a < b))

# c
print((a >= 18 and day == 3) != (a < 18 or day != 3))

# d
print((a >= 18 and day != 3) != (a < 18 or day == 3))
