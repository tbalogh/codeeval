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


