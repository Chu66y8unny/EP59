def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

x, y = 5, 0
result = divide(x, y)
if result is None:
    print('Invalid inputs')

x, y = 0, 5
result = divide(x, y)
if not result:
    print('Invalid inputs')  # This is wrong!


def divide(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None

x, y = 5, 0
success, result = divide(x, y)
if not success: 
    print('Invalid inputs')

x, y = 0, 5
_, result = divide(x, y)
if not result:
    print('Invalid inputs')  # This is wrong!


