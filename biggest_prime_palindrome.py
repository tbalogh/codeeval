
"""
Print out the biggest prime palindrome below the end
"""

end = 1000


def is_palindrome(text):
    text_len = len(text)
    for i in range(text_len / 2):
        if text[i] != text[text_len - 1 - i]:
            return False
    return True


def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def test_is_palindrome():
    palindromes = ["", "a", "aba", "ababa", "aa", "aaaaaa"]
    non_palindromes = ["ab, abb, ababab"]

    for palindrome in palindromes:
        assert is_palindrome(palindrome)

    for non_palindrome in non_palindromes:
        assert not is_palindrome(non_palindrome)


def test_is_prime():
    primes = [2, 7, 17, 31, 457, 521]
    non_primes = [0, 1, 10, 100, 1000]

    for prime in primes:
        assert is_prime(prime)

    for non_prime in non_primes:
        assert not is_prime(non_prime)

test_is_palindrome()
test_is_prime()

for i in range(end + 1, 1, -1):
    if is_palindrome(str(i)) and is_prime(i):
        print i
        break
