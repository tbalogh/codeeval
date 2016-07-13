

words = ['kajak', 'helo', '', 'aggregation']
reversed_words = ['kajak', 'oleh', '', 'noitagergga']


def reverse(word):
    return ''.join([word[i] for i in range(len(word) - 1, -1, -1)])


def test_reverse():
    for i in range(len(words)):
        # print words[i] + ': ' + reverse(words[i])
        assert reverse(words[i]) == reversed_words[i]

test_reverse()