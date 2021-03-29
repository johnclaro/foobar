#!/usr/bin/env python2

def solution(s):
    braille = init_braille()
    output = ''
    for letter in s:
        if letter.isupper():
            output += '000001'
        letter = letter.lower()
        output += braille[letter.lower()]
    return output


def init_braille():
    braille = {}
    sentence = 'the quick brown fox jumps over the lazy dog'
    output = '01111011001010001000000011111010100101010010010010100000000011' \
             '00001110101010100101111011100000001101001010101011010000000101' \
             '10101001101100111100011100000000101010111001100010111010000000' \
             '01111011001010001000000011100010000010101110111100000010011010' \
             '1010110110'
    step = 6
    words = [
        output[index:index + step]
        for index in range(0, len(output), step)
    ]
    for index, word in enumerate(words):
        letter = sentence[index]
        braille[letter] = word
    return braille


if __name__ == '__main__':
    output = solution('code')
    print output