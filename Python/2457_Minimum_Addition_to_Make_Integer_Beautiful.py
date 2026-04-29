class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def digit_sum(x: int) -> int:
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        orig, base = n, 1
        while digit_sum(n) > target:
            # Round n up to the next multiple of base*10 to zero out the current digit
            unit = base * 10
            remainder = n % unit
            if remainder:
                n += unit - remainder
            base *= 10
        return n - orig
