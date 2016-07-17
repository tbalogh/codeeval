'''

CHALLENGE DESCRIPTION:

The Fibonacci series is defined as: F(0) = 0; F(1) = 1; F(n) = F(n–1) + F(n–2) when n>1. Given an integer n≥0, print out the F(n).

INPUT SAMPLE:

The first argument will be a path to a filename containing integer numbers, one per line. E.g.

5
12
OUTPUT SAMPLE:

Print to stdout, the fibonacci number, F(n). E.g.

5
144

'''


fibonacci_map = {
    1: 1,   2: 2,   3: 3,
    4: 5,   5: 8,   6: 13,
    7: 21
}


def nth_fibonacci(n):
    if n == 1 or n == 2:
        return n

    previous = 0
    actual = 1

    for i in range(n-1):
        temp = actual
        actual += previous
        previous = temp

    return actual


def test_nth_fibonacci():
    for n, expected_result in fibonacci_map.items():
        # print str(n) + ': ' + str(nth_fibonacci(n))
        assert nth_fibonacci(n) == expected_result

# test_nth_fibonacci()

print nth_fibonacci(12)