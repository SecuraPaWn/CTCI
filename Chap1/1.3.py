"""1.3.py: Given two strings, write a method to decide if one is a permutation of the other."""
__author__ = 'karsaxen'


# This method uses sorting to check this
def checkForPermutationSort (s1,s2):

    if len(s1)!=len(s2):
        return False

    else:
        s1_sorted = sorted(s1)
        s2_sorted = sorted(s2)
        if s1_sorted == s2_sorted:
            return True
        else:
            return False

#O(N^2) - This method does not use sorting
def checkForPermutation(s1,s2):

    if len(s1)!=len(s2):
        return False

    else:
        for char in s1:
            if s2.find(char)==-1:
                return False
            else:
                s2 = s2.replace(char,"",1)
        return True

# Example of permutation
testTrue = ["brtghkit","hbrtgtik"]

# Example of not a permutation
testFalse = ["abcdefgh","ijklmnop"]

#Testing for Positive Test-case
if (checkForPermutationSort(testTrue[0],testTrue[1])):
    print("Test Passed!")
else:
    print("Test Failed!")

#Testing for Negative Test-csae
if not (checkForPermutationSort(testFalse[0],testFalse[1])):
    print("Test Passed!")
else:
    print("Test Failed!")

#Testing for Positive Test-case
if (checkForPermutation(testTrue[0],testTrue[1])):
    print("Test Passed!")
else:
    print("Test Failed!")

#Testing for Negative Test-csae
if not (checkForPermutation(testFalse[0],testFalse[1])):
    print("Test Passed!")
else:
    print("Test Failed!")






