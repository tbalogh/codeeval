

def is_prime(num):
    if num < 2:
        return False

    if num == 2:
        return True

    for i in range(2, num):
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

test_is_prime()