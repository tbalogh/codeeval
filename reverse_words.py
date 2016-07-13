

words = ['kajak', 'helo', '', 'aggregation']
reversed_words = ['kajak', 'oleh', '', 'noitagergga']


def reverse(word):
    return ''.join([word[i] for i in range(len(word) - 1, -1, -1)])


def test_reverse():
    for i in range(len(words)):
        assert reverse(words[i]) == reversed_words[i]