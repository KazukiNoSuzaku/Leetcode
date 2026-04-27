class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        target = bin(num2).count('1')
        current = bin(num1).count('1')
        x = num1
        # Remove excess high bits from num1
        for b in range(30):
            if current <= target:
                break
            if x >> b & 1:
                x ^= 1 << b
                current -= 1
        # Add missing low bits not in num1
        for b in range(30):
            if current >= target:
                break
            if not (x >> b & 1):
                x |= 1 << b
                current += 1
        return x
