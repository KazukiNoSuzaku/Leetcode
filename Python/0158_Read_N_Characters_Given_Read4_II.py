# The API: int read4(char *buf4) reads four consecutive characters from file, stores them
# in buf4, and returns the number of characters actually read.
# Use the API read4 to implement the function read(char *buf, int n) that reads n characters
# from file. This function may be called multiple times.

# Example 1:
# Input: file = "abc", queries = [1, 2, 1]
# Output: [1, 2, 0]

# Constraints:
# 1 <= file.length <= 500
# 1 <= queries.length <= 10
# 1 <= queries[i] <= 500

# Author: Kaustav Ghosh

def read4(buf4):
    pass  # provided by judge

class Solution(object):
    def __init__(self):
        self.buf4 = [''] * 4
        self.buf4_idx = 0
        self.buf4_count = 0

    def read(self, buf, n):
        total = 0
        while total < n:
            if self.buf4_idx == self.buf4_count:
                self.buf4_count = read4(self.buf4)
                self.buf4_idx = 0
                if self.buf4_count == 0:
                    break
            buf[total] = self.buf4[self.buf4_idx]
            self.buf4_idx += 1
            total += 1
        return total
