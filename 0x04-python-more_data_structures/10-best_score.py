#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    highscore_key = max(a_dictionary, key=a_dictionary.get)
    return highscore_key
