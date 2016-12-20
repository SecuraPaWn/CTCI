"""1.5.py: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string
aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the original string, your method should return
the original string"""

__author__ = 'karsaxen'

def returnCompressed(str):

    p1 = 0
    p2 = 0
    l = len(str)

    while p1 <= l and p2 <= l:
        c1 = str[p1]
        p2 = p1 + 1
        c2 = str[p2]

        while c1 == c2:
            c1 = str[p1]
            c2 = str[p2]
            p1 = p1 + 1
            p2 = p2 + 1

        p2 = p1
        count = 1 + p2 - p1
        print (count)

testString = "aabcccccaaa"
returnCompressed(testString)


