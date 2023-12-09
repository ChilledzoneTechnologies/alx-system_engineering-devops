#!/usr/bin/python3

def common_elements(set_1, set_2):
    newSet = {x for x in set_1 if x in set_2}
    return newSet
