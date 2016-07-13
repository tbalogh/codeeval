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

    n -= 2  # we handled the n == 1 and 2 case

    previous = 1
    actual = 2

    for i in range(n):
        temp = actual
        actual = previous + actual
        previous = temp

    return actual


def test_nth_fibonacci():
    for n, expected_result in fibonacci_map.items():
        # print str(n) + ': ' + str(nth_fibonacci(n))
        assert nth_fibonacci(n) == expected_result

test_nth_fibonacci()