class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        j = 0
        for c in str1:
            if j < len(str2):
                nxt = chr((ord(c) - ord('a') + 1) % 26 + ord('a'))
                if c == str2[j] or nxt == str2[j]:
                    j += 1
        return j == len(str2)
