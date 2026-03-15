# Return the number of distinct non-empty substrings of text that can be written
# as a concatenation of some string with itself (echo substring).

# Author: Kaustav Ghosh

class Solution(object):
    def distinctEchoSubstrings(self, text):
        n = len(text)
        seen = set()
        for length in range(1, n // 2 + 1):
            count = 0
            for i in range(n - length):
                if text[i] == text[i + length]:
                    count += 1
                else:
                    count = 0
                if count >= length:
                    seen.add(text[i + 1 - length: i + 1])
        return len(seen)
