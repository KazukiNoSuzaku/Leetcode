# Author: Kaustav Ghosh
# Problem: Number of Valid Words in a Sentence
# Approach: Validate each token: no digits; at most one hyphen and it must sit between two letters; at most one punctuation mark (!.,) and only as the final character. Count the tokens that pass

class Solution(object):
    def countValidWords(self, sentence):
        """
        :type sentence: str
        :rtype: int
        """
        punctuation = set('!.,')

        def valid(token):
            if not token:
                return False
            hyphens = 0
            puncts = 0
            for i, ch in enumerate(token):
                if ch.isdigit():
                    return False
                if ch == '-':
                    hyphens += 1
                    if hyphens > 1:
                        return False
                    if i == 0 or i == len(token) - 1 or not token[i - 1].isalpha() or not token[i + 1].isalpha():
                        return False
                elif ch in punctuation:
                    puncts += 1
                    if puncts > 1 or i != len(token) - 1:
                        return False
                elif not ch.islower():
                    return False
            return True

        return sum(1 for token in sentence.split() if valid(token))
