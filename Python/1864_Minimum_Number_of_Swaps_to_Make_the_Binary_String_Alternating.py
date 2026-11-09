# Author: Kaustav Ghosh
# Problem: Minimum Number of Swaps to Make the Binary String Alternating
# Approach: An alternating string of a given length fixes how many ones and zeros it must contain, so if the counts differ by more than one no rearrangement can work at all. Otherwise the target is determined up to which digit starts it: the more numerous digit has to go first, and when the counts are equal both starts are possible and the cheaper one wins. Against a fixed target, a swap repairs one misplaced one and one misplaced zero together, and the two kinds of mismatch are necessarily equal in number once the counts match, so the answer is simply half the mismatches.

class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        ones = s.count("1")
        zeros = len(s) - ones
        if abs(ones - zeros) > 1:
            return -1

        def swaps(first):
            wrong = 0
            for index, character in enumerate(s):
                expected = first if index % 2 == 0 else ("1" if first == "0" else "0")
                if character != expected:
                    wrong += 1
            return wrong // 2

        if ones > zeros:
            return swaps("1")
        if zeros > ones:
            return swaps("0")
        return min(swaps("0"), swaps("1"))
