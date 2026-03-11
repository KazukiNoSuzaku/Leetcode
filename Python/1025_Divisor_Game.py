# Alice and Bob play a game on number n. The player who cannot move loses.
# Alice wins if and only if n is even.

# Author: Kaustav Ghosh

class Solution(object):
    def divisorGame(self, n):
        return n % 2 == 0
