# We are playing the Guess Game. The game is as follows:
# I pick a number from 1 to n. You have to guess which number I picked.
# Every time you guess wrong, I will tell you whether the number I picked is
# higher or lower than your guess.
# You call a pre-defined API int guess(int num), which returns three possible results:
# -1: Your guess is higher than the number I picked (i.e. num > pick).
#  1: Your guess is lower than the number I picked (i.e. num < pick).
#  0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.

# Example 1:
# Input: n = 10, pick = 6
# Output: 6

# Constraints:
# 1 <= n <= 2^31 - 1
# 1 <= pick <= n

# Author: Kaustav Ghosh

class Solution(object):
    def guessNumber(self, n):
        lo, hi = 1, n
        while lo <= hi:
            mid = (lo + hi) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == 1:
                lo = mid + 1
            else:
                hi = mid - 1
