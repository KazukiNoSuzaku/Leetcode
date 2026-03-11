# A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings
# with their lengths. Given a string word and an abbreviation abbr, return whether the string
# matches the given abbreviation.

# Author: Kaustav Ghosh

class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        i = j = 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == '0':
                    return False
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                i += num
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        return i == len(word) and j == len(abbr)
