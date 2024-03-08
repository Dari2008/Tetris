def calculate_i(x, y):
    width = 10
    height = 15

    if y % 2 == 0:
        i = x + y
    else:
        i = width - x + y

    return i
