class Solution:
    def minimumOperations(self, num: str) -> int:
        n = len(num)
        res = n - 1 if '0' in num else n

        for target in ["00", "25", "50", "75"]:
            j = n - 1
            while j >= 0 and num[j] != target[1]:
                j -= 1
            if j < 0:
                continue
            i = j - 1
            while i >= 0 and num[i] != target[0]:
                i -= 1
            if i < 0:
                continue
            res = min(res, (n - 1 - j) + (j - 1 - i))

        return res
