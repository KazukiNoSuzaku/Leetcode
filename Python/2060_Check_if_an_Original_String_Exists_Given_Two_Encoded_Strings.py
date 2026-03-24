# Author: Kaustav Ghosh
# Problem 2060: Check if an Original String Exists Given Two Encoded Strings

class Solution(object):
    def possiblyEquals(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        def get_nums(s, i):
            """Get all possible numeric values starting at index i."""
            nums = set()
            val = 0
            while i < len(s) and s[i].isdigit():
                val = val * 10 + int(s[i])
                nums.add(val)
                i += 1
            return nums

        memo = {}

        def dp(i, j, diff):
            """
            i, j: indices into s1, s2
            diff: number of unmatched chars (positive = s1 ahead, negative = s2 ahead)
            """
            if (i, j, diff) in memo:
                return memo[(i, j, diff)]

            if i == len(s1) and j == len(s2):
                result = diff == 0
                memo[(i, j, diff)] = result
                return result

            # If s1 has digits, expand them
            if i < len(s1) and s1[i].isdigit():
                for num in get_nums(s1, i):
                    length = len(str(num)) if num < 10 else (2 if num < 100 else 3)
                    # Count actual digit chars consumed
                    k = i
                    v = 0
                    consumed = 0
                    while k < len(s1) and s1[k].isdigit():
                        v = v * 10 + int(s1[k])
                        consumed += 1
                        k += 1
                        if v == num:
                            if dp(k, j, diff + num):
                                memo[(i, j, diff)] = True
                                return True
                            break
                    # Try partial digit consumption
                    k = i
                    v = 0
                    while k < len(s1) and s1[k].isdigit():
                        v = v * 10 + int(s1[k])
                        k += 1
                        if dp(k, j, diff + v):
                            memo[(i, j, diff)] = True
                            return True
                memo[(i, j, diff)] = False
                return False

            if j < len(s2) and s2[j].isdigit():
                k = j
                v = 0
                while k < len(s2) and s2[k].isdigit():
                    v = v * 10 + int(s2[k])
                    k += 1
                    if dp(i, k, diff - v):
                        memo[(i, j, diff)] = True
                        return True
                memo[(i, j, diff)] = False
                return False

            # Both are letters or end
            if diff > 0 and j < len(s2):
                # s1 is ahead, consume from s2
                if dp(i, j + 1, diff - 1):
                    memo[(i, j, diff)] = True
                    return True
            elif diff < 0 and i < len(s1):
                # s2 is ahead, consume from s1
                if dp(i + 1, j, diff + 1):
                    memo[(i, j, diff)] = True
                    return True
            elif diff == 0 and i < len(s1) and j < len(s2):
                if s1[i] == s2[j]:
                    if dp(i + 1, j + 1, 0):
                        memo[(i, j, diff)] = True
                        return True

            memo[(i, j, diff)] = False
            return False

        return dp(0, 0, 0)
