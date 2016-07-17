'''

CHALLENGE DESCRIPTION:

Given a positive integer, find the sum of its constituent digits.

INPUT SAMPLE:

The first argument will be a path to a filename containing positive integers, one per line. E.g.

23
496
OUTPUT SAMPLE:

Print to stdout, the sum of the numbers that make up the integer, one per line. E.g.

5
19

'''

sum_of_digits_map = {
    123: 6,
    1: 1,
    2: 2,
    93: 12,
    5620394: 29
}


def sum_of_digits(num):
    return reduce(lambda x, y: x + y, [int(c) for c in str(num)])


def test_sum_of_digits():
    for num, expected_result in sum_of_digits_map.iteritems():
        # print str(num) + ': ' + str(sum_of_digits(num))
        assert sum_of_digits(num) == expected_result

test_sum_of_digits()