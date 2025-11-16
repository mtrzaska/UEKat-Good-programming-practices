# 1. Check if a string is a palindrome
def is_palindrome(text: str) -> bool:
    normalized = ''.join(char.lower() for char in text if char.isalnum())
    return normalized == normalized[::-1]

#2. Fibonacci number
def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# 3. Count vowels
def count_vowels(text: str) -> int:
    vowels = "aeiouyáéíóúýó"
    return sum(1 for char in text.lower() if char in vowels)

# 4. Calculate discount
def calculate_discount(price: float, discount: float) -> float:
    if not (0 <= discount <= 1):
        raise ValueError("Discount must be between 0 and 1")
    return price * (1 - discount)

# 5. Flatten list
def flatten_list(nested_list: list) -> list:
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened

# 6. Word frequencies
import string

def word_frequencies(text: str) -> dict:
    translator = str.maketrans("", "", string.punctuation)
    words = text.translate(translator).lower().split()
    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies

# 7. Check if a number is prime
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True