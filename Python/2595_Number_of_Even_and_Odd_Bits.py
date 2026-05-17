class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        even = odd = 0
        pos = 0
        while n:
            if n & 1:
                if pos % 2 == 0:
                    even += 1
                else:
                    odd += 1
            n >>= 1
            pos += 1
        return [even, odd]
