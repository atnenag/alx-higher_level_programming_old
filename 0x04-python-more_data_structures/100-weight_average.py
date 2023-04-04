#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    weight_total = 0
    weight_score_sum = 0
    for score, weight in my_list:
        weight_total += weight
        weight_score_sum += score * weight
    return weight_score_sum / weight_total
