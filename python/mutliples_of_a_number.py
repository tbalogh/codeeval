'''

CHALLENGE DESCRIPTION:

Given numbers x and n, where n is a power of 2, print out the smallest multiple of n which is greater than or equal to x. Do not use division or modulo operator.

INPUT SAMPLE:

The first argument will be a path to a filename containing a comma separated list of two integers, one list per line. E.g.

13,8
17,16
OUTPUT SAMPLE:

Print to stdout, the smallest multiple of n which is greater than or equal to x, one per line. E.g.

16
32

'''

import math


test_inputs = {
    7: 8, 8: 8, 9: 16, 127: 128, 128: 128, 129: 136
}

def multiples_of_a_number_greater_than(n, x):
    logn = int(math.log(n, 2))
    x_divided = x >> logn
    if x_divided * n == x:
        return x
    else:
        return x_divided * n + n


def test_multiples_of_a_number_greater_than():
    for n, expected_result in test_inputs.iteritems():
        assert multiples_of_a_number_greater_than(8, n) == expected_result


test_multiples_of_a_number_greater_than()


tests = ["13 8", "24 8"]

for test in tests:
    x, n = (int(num) for num in test.split(' ', 2))