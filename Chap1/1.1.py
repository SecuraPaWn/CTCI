"""Foobar.py: Implement algorithm to determine if string has unique characters."""
__author__ = 'karsaxen'

import unittest

def hasAllUniqueChars ( inputstr ) :
    #No Storage Used
    #O(n^2)

    for i in inputstr:
        isfound=0
        for j in inputstr:
            if i==j:
                isfound = isfound + 1
            if isfound>1:
                return False

    return True

def hasAllUniqueCharsSetmethod ( inputstr ) :
    #Hashtable used as a set data structure

    if (len(inputstr) > 256 ):
        return False

    if (len(inputstr) == len(set(inputstr))) :
        return True

testTrue = "abcdefghij"
testFalse = "aaasbyiyiu"

#Testing for Positive Test-case
if (hasAllUniqueChars(testTrue)):
    print("Test Passed!")
else:
    print("Test Failed!")

#Testing for Negative Test-csae
if not (hasAllUniqueChars(testFalse)):
    print("Test Passed!")
else:
    print("Test Failed!")

#Testing for Positive Test-case
if (hasAllUniqueCharsSetmethod(testTrue)):
    print("Test Passed!")
else:
    print("Test Failed!")

#Testing for Negative Test-csae
if not (hasAllUniqueCharsSetmethod(testFalse)):
    print("Test Passed!")
else:
    print("Test Failed!")