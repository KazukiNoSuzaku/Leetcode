# Author: Kaustav Ghosh
# Problem: Number of Valid Words in a Sentence
# Approach: Splitting on whitespace collapses any run of spaces and yields the tokens, after which each token is judged on its own against the three stated rules, all of which are local enough to settle in one left-to-right pass. A digit disqualifies the token outright. A hyphen must be the only one and must have a lowercase letter on each side, which also rules out a hyphen at either end. A punctuation mark must be the only one and must sit in the final position, which is what rejects a mark in the middle while still accepting a token that is nothing but a single mark. Anything surviving the pass is counted.

class Solution(object):
    def countValidWords(self, sentence):
        """
        :type sentence: str
        :rtype: int
        """
        def acceptable(token):
            hyphens = 0
            marks = 0
            last = len(token) - 1
            for index, char in enumerate(token):
                if char.isdigit():
                    return False
                if char == '-':
                    hyphens += 1
                    if hyphens > 1 or index == 0 or index == last:
                        return False
                    if not token[index - 1].islower() or not token[index + 1].islower():
                        return False
                elif char in '!.,':
                    marks += 1
                    if marks > 1 or index != last:
                        return False
            return True

        return sum(1 for token in sentence.split() if acceptable(token))
