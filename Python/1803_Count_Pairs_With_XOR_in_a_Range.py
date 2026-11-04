# Author: Kaustav Ghosh
# Problem: Count Pairs With XOR in a Range
# Approach: A range of XOR values is the difference of two prefix counts, so the whole problem reduces to counting pairs whose XOR is strictly below a bound, asked twice. For a fixed number that count is read off a binary trie of the numbers seen so far: descending bit by bit, wherever the bound has a 1 every number that makes this bit of the XOR a 0 is already guaranteed to be below the bound no matter what follows, so that entire subtree is added at once and the walk continues down the other branch. Inserting each number after it has been queried counts every pair exactly once, in O(15) work per number rather than comparing all pairs.

class Solution(object):
    def countPairs(self, nums, low, high):
        """
        :type nums: List[int]
        :type low: int
        :type high: int
        :rtype: int
        """
        BITS = 15  # both the values and high + 1 stay below 2 ** 15
        children = [[-1, -1]]
        subtree = [0]

        def insert(value):
            node = 0
            for bit in range(BITS - 1, -1, -1):
                side = value >> bit & 1
                step = children[node][side]
                if step < 0:
                    step = len(children)
                    children.append([-1, -1])
                    subtree.append(0)
                    children[node][side] = step
                node = step
                subtree[node] += 1

        def below(value, bound):
            node = 0
            found = 0
            for bit in range(BITS - 1, -1, -1):
                if node < 0:
                    break
                side = value >> bit & 1
                if bound >> bit & 1:
                    matching = children[node][side]
                    if matching >= 0:
                        found += subtree[matching]
                    node = children[node][side ^ 1]
                else:
                    node = children[node][side]
            return found

        answer = 0
        for value in nums:
            answer += below(value, high + 1) - below(value, low)
            insert(value)
        return answer
