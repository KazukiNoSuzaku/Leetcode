# Author: Kaustav Ghosh
class Solution(object):
    def minimumNumbers(self, num, k):
        # type: (int, int) -> int
        if num == 0:
            return 0
        for i in range(1, 11):
            val = i * k
            if val > num:
                break
            if val % 10 == num % 10:
                return i
        return -1
