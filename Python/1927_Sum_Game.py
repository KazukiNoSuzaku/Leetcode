# Author: Kaustav Ghosh
# Problem: Sum Game
# Approach: Split into halves and track each half's known-digit sum and number of '?'. If the total number of '?' is odd, Alice can always force a difference. Otherwise Bob (who wants equality) succeeds exactly when the known-sum gap already offsets the balanced fill 9*(cnt2-cnt1)/2

class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        half = len(num) // 2

        def scan(part):
            s = q = 0
            for ch in part:
                if ch == '?':
                    q += 1
                else:
                    s += int(ch)
            return s, q

        s1, q1 = scan(num[:half])
        s2, q2 = scan(num[half:])

        if (q1 + q2) % 2 == 1:
            return True
        # Bob equalizes iff s1 - s2 == 9 * (q2 - q1) / 2
        return 2 * (s1 - s2) != 9 * (q2 - q1)
