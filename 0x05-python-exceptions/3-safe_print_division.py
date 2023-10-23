#1/usr/bin/python3
def list_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print('Inside result: {}'.format(result))

    return result

