# Count groups of strings that can be made equal by swapping even/odd index chars.

# Author: Kaustav Ghosh

class Solution(object):
    def numSpecialEquivGroups(self, words):
        def signature(w):
            return (tuple(sorted(w[0::2])), tuple(sorted(w[1::2])))
        return len(set(signature(w) for w in words))
