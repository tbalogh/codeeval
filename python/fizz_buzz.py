'''

CHALLENGE DESCRIPTION:

Players generally sit in a circle. The first player says the number “1”, and each player says next number in turn. However, any number divisible by X (for example, three) is replaced by the word fizz, and any divisible by Y (for example, five) by the word buzz. Numbers divisible by both become fizz buzz. A player who hesitates, or makes a mistake is eliminated from the game.

Write a program that prints out the final series of numbers where those divisible by X, Y and both are replaced by “F” for fizz, “B” for buzz and “FB” for fizz buzz.

INPUT SAMPLE:

Your program should accept a file as its first argument. The file contains multiple separated lines; each line contains 3 numbers that are space delimited. The first number is the first divider (X), the second number is the second divider (Y), and the third number is how far you should count (N). You may assume that the input file is formatted correctly and the numbers are valid positive integers.

For example:


1
2
3 5 10
2 7 15
OUTPUT SAMPLE:

Print out the series 1 through N replacing numbers divisible by X with “F”, numbers divisible by Y with “B” and numbers divisible by both with “FB”. Since the input file contains multiple sets of values, your output should print out one line per set. Ensure that there are no trailing empty spaces in each line you print.


1
2
1 2 F 4 B F 7 8 F B
1 F 3 F 5 F B F 9 F 11 F 13 FB 15

'''

import sys


test_cases = [
    "3 5 10",
    "2 7 15",
    "",
    "2 3 6"
]

for test in test_cases:
    if not test:
        continue
    divider_first, divider_second, end = (int(x) for x in test.split(" ", 3))
    for i in range(1, end):
        if i % divider_first == 0 and i % divider_second == 0:
            sys.stdout.write('FB')
        elif i % divider_first == 0:
            sys.stdout.write('F')
        elif i % divider_second == 0:
            sys.stdout.write('B')
        else:
            sys.stdout.write(str(i))

        if i is not end:
            sys.stdout.write(' ')
            sys.stdout.flush()

    sys.stdout.write('\n')
    sys.stdout.flush()


