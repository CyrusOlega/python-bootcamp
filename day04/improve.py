def factorial(starting_num: int) -> int:
    """
    Finds the factorial of a given number.

    Example: The factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120
    :param starting_num:
    :return:
    """
    result: int = 1
    for index in range(1, starting_num + 1):
        result *= index

    return result


num: int = 5
factorial_result: int = factorial(num)
print(factorial_result)