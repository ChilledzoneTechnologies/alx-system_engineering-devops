#!/usr/bin/python3

def search_replace(my_list, search, replace):
    newList = my_list.copy()
    newList = list(map(lambda x: replace if x == search else x, newList))
    return newList
