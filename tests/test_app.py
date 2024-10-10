# test_app.py

import pytest

@pytest.fixture
def numbers():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_square_numbers(numbers):
    # Use map() with a lambda function to square each number
    squared_numbers = list(map(lambda x: x ** 2, numbers))
    expected_squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    assert squared_numbers == expected_squares

def test_filter_even_numbers(numbers):
    # Use filter() with a lambda function to filter out even numbers
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    expected_evens = [2, 4, 6, 8, 10]
    assert even_numbers == expected_evens
