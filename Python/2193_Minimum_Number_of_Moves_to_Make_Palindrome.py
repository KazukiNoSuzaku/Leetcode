# Author: Kaustav Ghosh
# Problem: Minimum Number of Moves to Make Palindrome
# Approach: Greedy two-pointer. For the left character, scan from the right end inward for its match; bring that match to the right position with adjacent swaps (counting them), then move both pointers inward. If the left character has no match, it is the unique middle character, so swap it one step toward the center and retry

class Solution(object):
    def minMovesToMakePalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        moves = 0
        i, j = 0, len(s) - 1
        while i < j:
            k = j
            while k > i and s[k] != s[i]:
                k -= 1
            if k == i:
                # s[i] is the odd one out; nudge it toward the center
                s[i], s[i + 1] = s[i + 1], s[i]
                moves += 1
            else:
                # bubble the matching char from k up to position j
                while k < j:
                    s[k], s[k + 1] = s[k + 1], s[k]
                    k += 1
                    moves += 1
                i += 1
                j -= 1
        return moves
