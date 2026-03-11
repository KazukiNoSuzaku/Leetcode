# We define the usage of capitals in a word to be right when one of the following cases holds:
# All letters are capitals, all letters are not capitals, or only the first letter is capital.
# Return true if the usage of capitals in this word is correct.

# Author: Kaustav Ghosh

class Solution(object):
    def detectCapitalUse(self, word):
        return word.isupper() or word.islower() or word.istitle()
