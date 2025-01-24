#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    highest_score = float('-inf')
    best_student = None

    for key, value in a_dictionary.items():
        if value > highest_score:
            highest_score = value
            best_student = key

    return best_student
