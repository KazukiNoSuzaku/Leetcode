# Author: Kaustav Ghosh
# Problem: Construct String With Repeat Limit
# Approach: Greedily append the largest available letter up to repeatLimit times. If that letter still has copies left, insert one copy of the next-largest available letter to break the run, then resume with the largest again. Stop when no larger filler exists

class Solution(object):
    def repeatLimitedString(self, s, repeatLimit):
        """
        :type s: str
        :type repeatLimit: int
        :rtype: str
        """
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        res = []
        i = 25  # current largest candidate
        while i >= 0:
            if cnt[i] == 0:
                i -= 1
                continue
            take = min(cnt[i], repeatLimit)
            res.append(chr(97 + i) * take)
            cnt[i] -= take
            if cnt[i] == 0:
                i -= 1
                continue
            # still copies of i left: need a smaller filler to break the run
            j = i - 1
            while j >= 0 and cnt[j] == 0:
                j -= 1
            if j < 0:
                break  # nothing smaller available; must stop
            res.append(chr(97 + j))
            cnt[j] -= 1
        return "".join(res)
