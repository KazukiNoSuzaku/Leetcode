# Given words and a result, check if letters can be mapped to digits (no leading zeros)
# such that the sum of words equals result.

# Author: Kaustav Ghosh

class Solution(object):
    def isSolvable(self, words, result):
        from itertools import permutations
        chars = list(set(''.join(words) + result))
        if len(chars) > 10:
            return False
        no_zero = set(w[0] for w in words + [result] if len(w) > 1)
        def check(mapping):
            def word_val(w):
                return int(''.join(str(mapping[c]) for c in w))
            return sum(word_val(w) for w in words) == word_val(result)
        for perm in permutations(range(10), len(chars)):
            mapping = dict(zip(chars, perm))
            if any(mapping[c] == 0 for c in no_zero):
                continue
            if check(mapping):
                return True
        return False
