class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for n in range(low, high + 1):
            s = str(n)
            if len(s) % 2 == 0:
                mid = len(s) // 2
                if sum(int(c) for c in s[:mid]) == sum(int(c) for c in s[mid:]):
                    ans += 1
        return ans
