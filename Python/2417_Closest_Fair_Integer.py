class Solution:
    def closestFair(self, n: int) -> int:
        def is_fair(x):
            s = str(x)
            odd = sum(int(c) % 2 for c in s)
            return odd * 2 == len(s)

        # Odd-digit numbers can never be fair; jump to next even-digit count
        while True:
            d = len(str(n))
            if d % 2 == 1:
                n = 10 ** d  # smallest number with d+1 digits
            elif is_fair(n):
                return n
            else:
                n += 1
