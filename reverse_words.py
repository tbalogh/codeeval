'''

REVERSE CHARACTERS IN WORDS

words = ['kajak', 'helo', '', 'aggregation']
reversed_words = ['kajak', 'oleh', '', 'noitagergga']


def reverse(word):
    return ''.join([word[i] for i in range(len(word) - 1, -1, -1)])


def test_reverse():
    for i in range(len(words)):
        # print words[i] + ': ' + reverse(words[i])
        assert reverse(words[i]) == reversed_words[i]
'''

test_inputs = {
    "Hello darkness my old friend": "friend old my darkness Hello",
    "": "",
    "This is an even length sentence": "sentence length even an is This"
}


def reverse_words_order_in_a_sentence(sentence):
    return ''.join(word + ' ' for word in reversed(sentence.split())).rstrip()


def test_reverse_words_order_in_a_sentence():
    for sentence, reversed_sentence in test_inputs.iteritems():
        # print "Result: " + reverse_words_order_in_a_sentence(sentence)
        # print "Expected: " + reversed_sentence
        assert reverse_words_order_in_a_sentence(sentence) == reversed_sentence

test_reverse_words_order_in_a_sentence()
print reverse_words_order_in_a_sentence("Hello world")


