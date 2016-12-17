"""1.4.py: Write a method to replace all spaces in a string with '%20'.You may assume that the string has sufficient space at the
end of the string to hold the additional characters, and that you are given the "true" length of the string.
EXAMPLE
Input: "Mr John Smith    "
Output: "Mr%20John%20Smith"

"""
__author__ = 'karsaxen'

import string


def replaceSpaceWithSpecial ( str ):

    # This removes the trailing space characters
    str = str.strip(" ")
    for c in str:
        if c==" ":
            #modified string after replacing the " " with "%20"
            mod_str = str.replace(c,'%20')
    print(mod_str)

testString = "Mr John Smith   "
replaceSpaceWithSpecial(testString)

