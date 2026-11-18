# Author: Kaustav Ghosh
# Problem: Minimum Garden Perimeter to Collect Enough Apples
# Approach: A square centred on the origin with corners at plus and minus n has a closed form for the apples inside it. Summing |i| + |j| over that square and collecting terms gives 2 * n * (n + 1) * (2 * n + 1), which grows cubically in n, so for 10^15 apples n stays under about 65000. The count is strictly increasing in n, so the smallest adequate square is found by binary search on n rather than by stepping, and the answer is its perimeter, 8 * n. Python's integers are exact, so the cubic product never overflows and no floating-point cube root is needed.

class Solution(object):
    def minimumPerimeter(self, neededApples):
        """
        :type neededApples: int
        :rtype: int
        """
        def apples(half):
            return 2 * half * (half + 1) * (2 * half + 1)

        low, high = 1, 1
        while apples(high) < neededApples:
            high *= 2
        while low < high:
            middle = (low + high) // 2
            if apples(middle) >= neededApples:
                high = middle
            else:
                low = middle + 1
        return 8 * low
