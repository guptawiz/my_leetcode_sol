# Given a string, find the index of the first non-repeating character in it and return it. If it doesn't exist, return -1.
# Note:
# Try not to use any in-built functions like find(), first(), ListToSet (), Convert to Set () etc.
# Please read the sample input and output below to understand the question better.
#
# Input1:"heyhello"
# Output1: 2
#
# Input2: "netsetonset"
# Output2: 6

def non_rep(x):
    y = list(x)
    for i in y:
        if i in y[i:]:
            continue
        else:
            return y[i]
    return -1

non_rep("hello")