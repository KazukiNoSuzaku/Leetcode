class Solution:
    def smallestNumber(self, pattern: str) -> str:
        # Stack: push digits 1..n+1; on 'I' or end, flush stack to result
        result = []
        stack = []
        for i, ch in enumerate(pattern + 'I'):
            stack.append(i + 1)
            if ch == 'I':
                result.extend(reversed(stack))
                stack = []
        return ''.join(map(str, result))
