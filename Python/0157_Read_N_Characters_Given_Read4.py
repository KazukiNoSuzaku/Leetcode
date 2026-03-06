# The API: int read4(char *buf4) reads four consecutive characters from file, stores them
# in buf4, and returns the number of characters actually read.
# Use the API read4 to implement the function read(char *buf, int n) that reads n characters
# from file. This function is called only once.

# Example 1:
# Input: file = "abc", n = 4
# Output: 3
# Explanation: After calling your read method, buf should contain "abc". We read 3 characters.

# Constraints:
# 1 <= file.length <= 500
# file consist of English letters and digits.
# 1 <= n <= 1000

# Author: Kaustav Ghosh

def read4(buf4):
    pass  # provided by judge

class Solution(object):
    def read(self, buf, n):
        total = 0
        buf4 = [''] * 4
        while total < n:
            count = read4(buf4)
            count = min(count, n - total)
            for i in range(count):
                buf[total + i] = buf4[i]
            total += count
            if count < 4:
                break
        return total
