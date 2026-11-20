# Author: Kaustav Ghosh
# Problem: Number of Ways to Separate Numbers
# Approach: A split is determined by the lengths of its parts, and the non-decreasing requirement only ever compares a part with the one immediately before it, so the state is how much of the string is used and how long the last part is. If the previous part is strictly shorter it is automatically smaller, since no part may carry a leading zero, so only equal lengths need an actual comparison of the two substrings. Writing the table in terms of running sums over the last part's length turns the transition into: the ways ending with a part of this length equal the ways for the earlier prefix with a strictly shorter last part, plus, when the two equal-length substrings compare the right way, the ways with an equally long last part; both of those are entries of the running-sum column for this length or the one before, so iterating over lengths on the outside keeps just two columns in memory instead of a full n by n table. The equal-length comparison is resolved in constant time from a longest-common-prefix array for the current offset, which itself is one backward pass, giving O(n^2) time and O(n) space.

class Solution(object):
    def numberOfCombinations(self, num):
        """
        :type num: str
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        total = len(num)
        if num[0] == '0':
            return 0

        zero = [c == '0' for c in num]

        previous = [0] * (total + 1)
        previous[0] = 1

        for width in range(1, total + 1):
            shared = [0] * (total + 1)
            for start in range(total - width - 1, -1, -1):
                if num[start] == num[start + width]:
                    shared[start] = shared[start + 1] + 1

            current = [0] * (total + 1)
            current[0] = 1
            for used in range(1, total + 1):
                carried = previous[used]
                if used >= width and not zero[used - width]:
                    earlier = used - width
                    if earlier >= width:
                        front = earlier - width
                        common = shared[front]
                        if common >= width or num[front + common] <= num[earlier + common]:
                            carried += current[earlier]
                        else:
                            carried += previous[earlier]
                    else:
                        carried += previous[earlier]
                current[used] = carried % MOD
            previous = current

        return previous[total]
