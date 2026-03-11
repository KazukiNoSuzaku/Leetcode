# Given a string s, check if it can be constructed by taking a substring of it
# and appending multiple copies of the substring together.

# Author: Kaustav Ghosh

class Solution(object):
    def repeatedSubstringPattern(self, s):
        return s in (s + s)[1:-1]
