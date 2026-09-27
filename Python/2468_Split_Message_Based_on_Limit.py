# Author: Kaustav Ghosh
# Problem: Split Message Based on Limit
# Approach: Fix the number of parts b and every suffix length is known: part i carries "<i/b>", so its room for text is limit - 3 - len(str(i)) - len(str(b)). Summing that over all parts, with a running total of the digit lengths, gives b's total capacity in constant time, and b is only usable when even the longest-numbered part has room for a character. Take the smallest workable b and fill each part to the brim

class Solution(object):
    def splitMessage(self, message, limit):
        """
        :type message: str
        :type limit: int
        :rtype: List[str]
        """
        n = len(message)
        digit_total = 0
        for parts in range(1, n + 2):
            width = len(str(parts))
            digit_total += width
            fixed = 3 + width
            if limit - fixed - width < 1:
                continue
            if parts * (limit - fixed) - digit_total >= n:
                pieces = []
                position = 0
                for i in range(1, parts + 1):
                    take = limit - fixed - len(str(i))
                    pieces.append("%s<%d/%d>" % (message[position:position + take], i, parts))
                    position += take
                return pieces
        return []
