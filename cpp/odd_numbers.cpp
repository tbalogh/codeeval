//
// Created by Tamas Balogh on 17/07/16.
//

/* EXERCISE

Print the odd numbers from 1 to 99.

INPUT SAMPLE:

There is no input for this program.

OUTPUT SAMPLE:

Print the odd numbers from 1 to 99, one number per line.

*/


#include "odd_numbers.h"

#include <iostream>

using namespace std;

void printOddNumbers(int until) {
    for (int i = 1; i < until; i += 2) {
        cout << i << endl;
    }
}