'''

1, 2, 3, 5, 8, 13, 21, ...

'''


fibonacci_map = {
    1: 1,   2: 2,   3: 3,
    4: 5,   5: 8,   6: 13,
    7: 21
}


def nth_fibonacci(n):
    if n == 1 or n == 2:
        return n

    first = 1
    second = 2
    n -= 2

    for i in range(n):
        temp = second
        second = first + second
        first = temp

    return second


def test_nth_fibonacci():
    for key, val in fibonacci_map:
        assert nth_fibonacci(key) == val