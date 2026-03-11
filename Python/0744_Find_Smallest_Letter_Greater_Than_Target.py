# Find smallest letter in sorted circular array greater than target.

# Author: Kaustav Ghosh

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        for l in letters:
            if l > target: return l
        return letters[0]
