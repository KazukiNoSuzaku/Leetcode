class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        # min_suffix[i] = smallest char in s[i:]
        min_suffix = [''] * (n + 1)
        min_suffix[n] = chr(ord('z') + 1)
        for i in range(n - 1, -1, -1):
            min_suffix[i] = min(s[i], min_suffix[i + 1])

        result = []
        stack = []
        for i, ch in enumerate(s):
            stack.append(ch)
            while stack and stack[-1] <= min_suffix[i + 1]:
                result.append(stack.pop())
        return ''.join(result)
