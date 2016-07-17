'''

CHALLENGE DESCRIPTION:

Write a program which reverses the words in an input sentence.

INPUT SAMPLE:

The first argument is a file that contains multiple sentences, one per line. Empty lines are also possible.

For example:


1
2
Hello World
Hello CodeEval
OUTPUT SAMPLE:

Print to stdout each sentence with the reversed words in it, one per line. Empty lines in the input should be ignored. Ensure that there are no trailing empty spaces in each line you print.

For example:


1
2
World Hello
CodeEval Hello


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


