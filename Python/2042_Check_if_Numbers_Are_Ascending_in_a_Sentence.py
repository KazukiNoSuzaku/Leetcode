# Author: Kaustav Ghosh
# Problem: Check if Numbers Are Ascending in a Sentence
# Approach: Splitting on whitespace gives the tokens, each of which is either a word of letters or a number, so a token is numeric exactly when it consists of digits. Only the numeric tokens matter and they must rise strictly, which needs just the previous number rather than the whole list: each new number is compared against it and anything not strictly larger settles the answer immediately. Starting the comparison below the smallest possible value lets the first number pass without a special case, since every number in the sentence is positive.

class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        previous = 0
        for token in s.split():
            if token.isdigit():
                value = int(token)
                if value <= previous:
                    return False
                previous = value
        return True
