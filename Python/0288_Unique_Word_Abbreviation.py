# An abbreviation of a word follows the form: [first letter]...[number of letters removed]..[last letter].
# A word's abbreviation is valid if no other word in the dictionary has the same abbreviation.
# Implement the ValidWordAbbr class:
# - ValidWordAbbr(String[] dictionary) initializes the object with a dictionary of words.
# - boolean isUnique(String word) returns true if either the word is not in the dictionary,
#   or there is no other word in the dictionary with the same abbreviation as word.

# Example 1:
# Input: ["ValidWordAbbr","isUnique","isUnique","isUnique","isUnique","isUnique"]
#        [[["deer","door","cake","card"]],["dear"],["cart"],["cane"],["make"],["cake"]]
# Output: [null,false,true,false,true,true]

# Constraints:
# 1 <= dictionary.length <= 3 * 10^4

# Author: Kaustav Ghosh

class ValidWordAbbr(object):
    def __init__(self, dictionary):
        self.abbr = {}
        for w in dictionary:
            a = self._abbrev(w)
            if a not in self.abbr:
                self.abbr[a] = w
            elif self.abbr[a] != w:
                self.abbr[a] = None

    def _abbrev(self, w):
        return w if len(w) <= 2 else w[0] + str(len(w) - 2) + w[-1]

    def isUnique(self, word):
        a = self._abbrev(word)
        return a not in self.abbr or self.abbr[a] == word
