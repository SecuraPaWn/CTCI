"""1.8.py: Assume you have a method isSubstring which checks if one word is a substring of another. Given two
strings, s1 and s2, write code to check is s2 is a rotation of s1 using only one call to isSubstring (e.g., "waterbottle" is a
rotation of s1 using only one call to isSubstring (e.g "waterbottle" is a rotation of "erbottlewat") """
__author__ = 'karsaxen'

def isSubstring(s1,s2):

    x = s1.find(s2)
    if x != -1:
        return True
    else:
        return False

def isMirrorSubstring(s1,s2):

    #Doubling of the string ensures the mirror string to to detected by Substring function
    s1 = s1 + s1;
    x = s1.find(s2)
    if x != -1:
        return True
    else:
        return False

s1="Hello World"
s2="World"
bool = isSubstring(s1,s2)
print(bool)

s1="waterbottle"
s2="erbottlewat"
bool = isMirrorSubstring(s1,s2)
print(bool)

