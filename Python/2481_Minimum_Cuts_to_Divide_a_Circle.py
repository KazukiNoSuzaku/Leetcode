class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1:
            return 0
        # Even n: n/2 diameters produce n equal slices.
        # Odd n: n radial cuts (each chord goes to the center) are required.
        return n // 2 if n % 2 == 0 else n
