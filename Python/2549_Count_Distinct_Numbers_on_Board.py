class Solution:
    def distinctIntegers(self, n: int) -> int:
        # Each day every x on board adds x-1 if n%x==0; after enough days board = {2..n}; answer = n-1.
        return max(1, n - 1)
