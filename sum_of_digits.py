

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