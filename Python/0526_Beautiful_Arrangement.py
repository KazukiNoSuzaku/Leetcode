# Suppose you have n integers labeled 1 through n. A permutation perm is called beautiful
# if for every i (1 <= i <= n), either perm[i] is divisible by i or i is divisible by perm[i].
# Return the number of beautiful arrangements.

# Author: Kaustav Ghosh

class Solution(object):
    def countArrangement(self, n):
        self.res = 0
        def backtrack(pos, used):
            if pos > n:
                self.res += 1
                return
            for num in range(1, n + 1):
                if num not in used and (num % pos == 0 or pos % num == 0):
                    used.add(num)
                    backtrack(pos + 1, used)
                    used.remove(num)
        backtrack(1, set())
        return self.res
