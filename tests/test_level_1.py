import pytest

from c1 import solution


@pytest.fixture
def braille():
    braille = {
        "a": "100000", 
        "b": "110000", 
        "c": "100100", 
        "d": "100110", 
        "e": "100010", 
        "f": "110100", 
        "g": "110110", 
        "h": "110010", 
        "i": "010100", 
        "j": "010110", 
        "k": "101000", 
        "l": "111000", 
        "m": "101100", 
        "n": "101110", 
        "o": "101010", 
        "p": "111100", 
        "q": "111110", 
        "r": "111010", 
        "s": "011100", 
        "t": "011110", 
        "u": "101001", 
        "v": "111001", 
        "w": "010111", 
        "x": "101101", 
        "y": "101111", 
        "z": "101011"
    }
    return braille


def test_1():
    output = solution('code')
    expected = '100100101010100110100010'
    assert output == expected


def test_2():
    output = solution('The quick brown fox jumps over the lazy dog')
    expected = '000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110'
    assert output == expected


def test_3():
    output = solution('Braille')
    expected = '000001110000111010100000010100111000111000100010'
    assert output == expected


def test_4(braille):
    output = solution('a')
    expected = braille['a']
    assert output == expected


def test_5(braille):
    output = solution('A')
    expected = '000001%s'.format(braille['a'])
    assert output == expected


def test_5(braille):
    output = solution('Maecenas cursus libero sed fermentum orci aliquamo')
    expected = '000001101100100000100010100100100010101110100000011100000000100100101001111010011100101001011100000000111000010100110000100010111010101010000000011100100010100110000000110100100010111010101100100010101110011110101001101100000000101010111010100100010100000000100000111000010100111110101001100000101100101010'
    assert output == expected
