# Author: Kaustav Ghosh

class Solution(object):
    def minMovesToMakePalindrome(self, s):
        # type: (str) -> int
        s = list(s)
        moves = 0
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # Find match for s[left] from right side
                k = right
                while k > left and s[k] != s[left]:
                    k -= 1
                if k == left:
                    # s[left] is the middle element, swap it one step right
                    s[left], s[left + 1] = s[left + 1], s[left]
                    moves += 1
                else:
                    # Bring s[k] to right by swapping
                    while k < right:
                        s[k], s[k + 1] = s[k + 1], s[k]
                        k += 1
                        moves += 1
                    left += 1
                    right -= 1

        return moves
