side_a = 5
side_b = 4
side_c = 3
epsilon = 1e-7

if side_a > side_c:                     # is side_a is larger than side_c, swap values
    side_a, side_c = side_c, side_a

if side_b > side_c:
    side_b, side_c = side_c, side_b

# now side_c must be the largest

sum_squares = (side_a ** 2) + (side_b ** 2)
hypotenues_square = side_c ** 2

if abs(sum_squares - hypotenues_square) < epsilon:
    print("This is a right angled triangle")
else:
    print("This is not a right angled triangle")
