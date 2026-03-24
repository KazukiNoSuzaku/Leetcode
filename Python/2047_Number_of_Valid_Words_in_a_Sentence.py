# Author: Kaustav Ghosh
# Problem 2047: Number of Valid Words in a Sentence

class Solution(object):
    def countValidWords(self, sentence):
        """
        :type sentence: str
        :rtype: int
        """
        count = 0
        for token in sentence.split():
            if self._is_valid(token):
                count += 1
        return count

    def _is_valid(self, token):
        has_hyphen = False
        n = len(token)
        for i, c in enumerate(token):
            if c.isdigit():
                return False
            if c == '-':
                if has_hyphen:
                    return False
                has_hyphen = True
                if i == 0 or i == n - 1:
                    return False
                if not token[i - 1].isalpha() or not token[i + 1].isalpha():
                    return False
            if c in ('!', '.', ','):
                if i != n - 1:
                    return False
        return True
