# Author: Kaustav Ghosh
# Problem: Construct the Lexicographically Largest Valid Sequence
# Approach: Lexicographically largest means the earliest slot should hold the biggest value that can possibly work, so the search fills positions left to right and tries values from n downwards, committing to the first that lets the rest of the sequence complete. Placing a value fixes both of its occurrences at once, since their separation is dictated by the value itself, which is what makes each attempt cheap to make and to undo. The value one appears only once, so it is handled on its own. Because the first success at each position is already the largest possible, no comparison between completed sequences is ever needed.

class Solution(object):
    def constructDistancedSequence(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        size = 2 * n - 1
        slots = [0] * size
        used = [False] * (n + 1)

        def fill(at):
            if at == size:
                return True
            if slots[at]:
                return fill(at + 1)
            for value in range(n, 0, -1):
                if used[value]:
                    continue
                partner = at if value == 1 else at + value
                if partner >= size or slots[partner]:
                    continue
                used[value] = True
                slots[at] = slots[partner] = value
                if fill(at + 1):
                    return True
                slots[at] = slots[partner] = 0
                used[value] = False
            return False

        fill(0)
        return slots
