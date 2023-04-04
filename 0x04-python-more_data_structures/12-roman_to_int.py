#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    a_dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer_value = 0
    given = 0
    for char in roman_string[::-1]:
        value = a_dictionary[char]
        if value < given:
            integer_value -= value
        else:
            integer_value += value
        given = value
    return integer_value
