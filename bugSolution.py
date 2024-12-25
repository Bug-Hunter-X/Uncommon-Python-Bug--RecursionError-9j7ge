def my_function(x):
    if x == 0:
        return 0
    elif x < 0:
        return 0  # Handle negative inputs
    else:
        return my_function(x - 1) + x