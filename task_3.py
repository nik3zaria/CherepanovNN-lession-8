def type_of_variables(func):
    def additional_function(*args):
        for arg in args:
            print(f'{arg}: {type(arg)}')
        result = func(*args)
        return result

    return additional_function


@type_of_variables
def exponentiation(x, y):
    if (type(y) == int and type(x) == int):
        return x ** y
    else:
        return print('У одной из переменных не числовой тип данных')


print(exponentiation('4', 15))