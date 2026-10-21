# Author: Kaustav Ghosh
# Problem: Defuse the Bomb
# Approach: Every answer is a sum of the same number of consecutive entries, just taken from a different starting offset, so rather than re-adding k entries for each position I slide one window around the circle: the window for the next position drops one end and gains the other, which makes the whole pass linear instead of quadratic. The sign of k only decides where the window sits relative to the position, ahead of it or behind it, and the circular wrap is handled by taking indices modulo the length. A k of zero is its own case and simply yields zeros.

class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(code)
        if k == 0:
            return [0] * n

        width = abs(k)
        # Window for position 0: the next k entries, or the previous |k| entries.
        start = 1 if k > 0 else n - width
        running = sum(code[(start + j) % n] for j in range(width))
        answer = [0] * n
        for i in range(n):
            answer[i] = running
            # Advance both ends of the window by one position.
            running -= code[(start + i) % n]
            running += code[(start + i + width) % n]
        return answer
