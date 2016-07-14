from math import sqrt


def is_prime(num):
    if num < 2:
        return False

    if num == 2:
        return True

    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


def test_is_prime():
    primes = [2, 7, 17, 31, 457, 521]
    non_primes = [0, 1, 10, 100, 1000]

    for prime in primes:
        assert is_prime(prime)

    for non_prime in non_primes:
        assert not is_prime(non_prime)


# def sum_of_primes_until(num):
#     sum = 0
#     for i in range(0, num + 1):
#         if is_prime(i):
#             sum += i
#     return sum


# def sum_of_primes_until(num):
#     return reduce(lambda x, y: x + y if is_prime(y) else x, range(num + 1))


# print sum_of_primes_until(1000)

def sum_of_first_n_primes(n):
    prime_counter = 0
    sum_of_primes = 0
    i = 0
    while prime_counter < n:
        if is_prime(i):
            sum_of_primes += i
            prime_counter += 1
        i += 1

    return sum_of_primes

print sum_of_first_n_primes(1000)
