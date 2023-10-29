#Write a function 'oddCounter' which takes a list of numbers as an argument and counts how many odd numbers are in it.
#You can only use lambda functions and HOFs: takewhile, dropwhile, zip, filter, map, reduce, enumerate, any, all, sum.
#You are not allowed to use for and while loops.

def oddCounter(numList):
    return sum(map(lambda x: x % 2, numList))
