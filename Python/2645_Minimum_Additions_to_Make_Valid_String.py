class Solution:
    def addMinimum(self, word: str) -> int:
        additions = 0
        pos = 0  # position within current "abc" block (0,1,2)
        for c in word:
            p = ord(c) - ord('a')
            if p < pos:
                additions += 3 - pos  # complete the current block
                pos = 0
            additions += p - pos  # insert missing chars before c in this block
            pos = p + 1
            if pos == 3:
                pos = 0
        if pos > 0:
            additions += 3 - pos  # complete the last block
        return additions
