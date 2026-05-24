class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        s = list(s)
        n = len(s)
        i = n - 1

        while i >= 0:
            s[i] = chr(ord(s[i]) + 1)
            if ord(s[i]) - ord('a') >= k:
                i -= 1
                continue
            if (i >= 1 and s[i] == s[i - 1]) or (i >= 2 and s[i] == s[i - 2]):
                continue
            # Fill the rest greedily with the smallest valid char
            for j in range(i + 1, n):
                for c in 'abcdefghijklmnopqrstuvwxyz'[:k]:
                    if (j < 1 or c != s[j - 1]) and (j < 2 or c != s[j - 2]):
                        s[j] = c
                        break
            return ''.join(s)

        return ""
