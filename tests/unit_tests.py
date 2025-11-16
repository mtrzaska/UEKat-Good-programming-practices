import sys
import os

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
print(f"Adding {src_path} to sys.path")
sys.path.insert(0, src_path)

import pytest
from src.functions import (
    is_palindrome,
    fibonacci,
    count_vowels,
    calculate_discount,
    flatten_list,
    word_frequencies,
    is_prime,
)

# 1. Test is_palindrome
@pytest.mark.parametrize("text,expected", [
    ("kajak", True),
    ("Kobyła ma mały bok", True),
    ("python", False),
    ("", True),
    ("A", True),
])
def test_is_palindrome(text, expected):
    assert is_palindrome(text) == expected

# 2. Test fibonacci
@pytest.mark.parametrize("n,expected", [
    (0, 0),
    (1, 1),
    (5, 5),
    (10, 55),
])
def test_fibonacci(n, expected):
    assert fibonacci(n) == expected

def test_fibonacci_negative():
    with pytest.raises(ValueError):
        fibonacci(-1)

# 3. Test count_vowels
@pytest.mark.parametrize("text,expected", [
    ("Python", 1),
    ("AEIOUY", 6),
    ("bcd", 0),
    ("", 0),
    ("Próba żółwia", 4),
])
def test_count_vowels(text, expected):
    assert count_vowels(text) == expected

# 4. Test calculate_discount
@pytest.mark.parametrize("price,discount,expected", [
    (100, 0.2, 80.0),
    (50, 0, 50.0),
    (200, 1, 0.0),
])
def test_calculate_discount(price, discount, expected):
    assert calculate_discount(price, discount) == pytest.approx(expected)

@pytest.mark.parametrize("price,discount", [
    (100, -0.1),
    (100, 1.5),
])
def test_calculate_discount_invalid(price, discount):
    with pytest.raises(ValueError):
        calculate_discount(price, discount)

# 5. Test flatten_list
@pytest.mark.parametrize("nested_list,expected", [
    ([1, 2, 3], [1, 2, 3]),
    ([1, [2, 3], [4, [5]]], [1, 2, 3, 4, 5]),
    ([], []),
    ([[[1]]], [1]),
    ([1, [2, [3, [4]]]], [1, 2, 3, 4]),
])
def test_flatten_list(nested_list, expected):
    assert flatten_list(nested_list) == expected

# 6. Test word_frequencies
@pytest.mark.parametrize("text,expected", [
    ("To be or not to be", {"to": 2, "be": 2, "or": 1, "not": 1}),
    ("Hello, hello!", {"hello": 2}),
    ("", {}),
    ("Python Python python", {"python": 3}),
    ("Ala ma kota, a kot ma Ale.", {"ala": 1, "ma": 2, "kota": 1, "a": 1, "kot": 1, "ale": 1}),
])
def test_word_frequencies(text, expected):
    assert word_frequencies(text) == expected

# 7. Test is_prime
@pytest.mark.parametrize("n,expected", [
    (2, True),
    (3, True),
    (4, False),
    (0, False),
    (1, False),
    (97, True),
])
def test_is_prime(n, expected):
    assert is_prime(n) == expected