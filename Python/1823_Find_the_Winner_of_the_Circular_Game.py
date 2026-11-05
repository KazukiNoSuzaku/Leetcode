# Author: Kaustav Ghosh
# Problem: Find the Winner of the Circular Game
# Approach: This is the Josephus problem. After the first friend is eliminated the remaining n - 1 sit in the same kind of circle, just renumbered so that counting restarts from the person after the one removed, which means the winner's position for n follows from the winner's position for n - 1 by shifting forward k places and wrapping. Building that up from a circle of one gives the answer in n steps with no list to rotate or delete from, and the final shift by one converts the zero-based position to the friend's label.

class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        winner = 0
        for size in range(2, n + 1):
            winner = (winner + k) % size
        return winner + 1
