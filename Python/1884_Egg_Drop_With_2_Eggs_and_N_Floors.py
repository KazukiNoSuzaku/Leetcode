# Author: Kaustav Ghosh
# Problem: Egg Drop With 2 Eggs and N Floors
# Approach: With a budget of k drops, the first egg should be tried at floor k, because if it breaks the second egg must sweep the k - 1 floors below one at a time and that uses the remaining budget exactly. If it survives, the next trial is k - 1 floors higher, since one drop has been spent, and so on. The floors covered by k drops are therefore k plus k - 1 plus the rest down to one, which is k times k plus one over two, so the answer is the smallest k whose triangular number reaches n.

class Solution(object):
    def twoEggDrop(self, n):
        """
        :type n: int
        :rtype: int
        """
        drops = 1
        while drops * (drops + 1) // 2 < n:
            drops += 1
        return drops
