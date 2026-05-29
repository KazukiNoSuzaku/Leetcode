class Solution:
    def isFascinating(self, n: int) -> bool:
        s = str(n) + str(2 * n) + str(3 * n)
        return len(s) == 9 and set(s) == set('123456789')
