#!/usr/bin/env python2

def solution(sentence):
    braille = setup()
    output = ''
    for letter in sentence:
        if letter.isupper():
            output += '000001'
        elif letter.isspace():
            output += '000000'
        if not letter.isspace():
            output += braille[letter.lower()]
    return output


def setup():
    braille = {}
    sentence = 'The quick brown fox jumps over the lazy dog'
    output = '000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110'
    step = 6
    words = [
        output[index:index + step]
        for index in range(0, len(output), step)
    ]
    for index, word in enumerate(words):
        if word not in ('000001', '000000',):
            letter = sentence[index - 1]
            letter = letter.lower()
            braille[letter] = word
    return braille


if __name__ == '__main__':
    solution('code')
    solution('The quick brown fox jumps over the lazy dog')
    solution('Braille')
