class Solution:
    def finalString(self, s: str) -> str:
        result = []
        for c in s:
            if c == 'i':
                result.reverse()
            else:
                result.append(c)
        return ''.join(result)
