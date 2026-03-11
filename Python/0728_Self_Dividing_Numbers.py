# Find all self-dividing numbers in range [left, right].

# Author: Kaustav Ghosh

class Solution(object):
    def selfDividingNumbers(self, left, right):
        def is_self_dividing(n):
            for d in str(n):
                if d == '0' or n % int(d) != 0: return False
            return True
        return [n for n in range(left, right + 1) if is_self_dividing(n)]
