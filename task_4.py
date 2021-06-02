def val_checker(is_valid):
    def additional_function(func):
        def validity_check(*args):
            if is_valid(*args):
                result = func(*args)
                return print(result)
            else:
                raise ValueError
        return validity_check
    return additional_function


def func_valid(integer):
    return 0 < integer


@val_checker(func_valid)
def calc_cube(x):
    return x ** 3


calc_cube(20)