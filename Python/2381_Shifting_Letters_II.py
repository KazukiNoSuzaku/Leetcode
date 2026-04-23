class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)
        for l, r, d in shifts:
            delta = 1 if d else -1
            diff[l] += delta
            diff[r + 1] -= delta
        result = []
        total = 0
        for i, ch in enumerate(s):
            total += diff[i]
            result.append(chr((ord(ch) - ord('a') + total) % 26 + ord('a')))
        return ''.join(result)
