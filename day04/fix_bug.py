def find_even_numbers(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens

def test_find_even_numbers():
    numbers = [1, 2, 3, 4, 5, 6]
    assert find_even_numbers(numbers) == [2,4,6]