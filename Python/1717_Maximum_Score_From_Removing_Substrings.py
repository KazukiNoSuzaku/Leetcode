# Author: Kaustav Ghosh
# Problem: Maximum Score From Removing Substrings
# Approach: Removing the better-paying pair first is always at least as good, because any occurrence of the cheaper pair that this destroys could only have been formed from letters that the expensive removal also consumes, so nothing is lost by being greedy about which pattern goes first. Normalising so that the first letter of the better-paying pair is the one counted lets a single scan do both passes at once: the first letter is stacked, the second cancels against a waiting first for the higher score, and any second letter with nothing to cancel waits for the cheaper pairing. Characters outside the two letters are barriers that nothing can cross, so the pending counts are settled and reset there.

class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        first, second = 'a', 'b'
        if x < y:
            x, y = y, x
            first, second = second, first

        score = 0
        pending_first = 0
        pending_second = 0
        for ch in s:
            if ch == first:
                pending_first += 1
            elif ch == second:
                if pending_first:
                    pending_first -= 1
                    score += x
                else:
                    pending_second += 1
            else:
                # Neither letter can pair across a foreign character.
                score += min(pending_first, pending_second) * y
                pending_first = pending_second = 0
        score += min(pending_first, pending_second) * y
        return score
